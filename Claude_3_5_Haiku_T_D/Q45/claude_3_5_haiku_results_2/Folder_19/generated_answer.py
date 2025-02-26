from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def can_form_palindrome(freq):
        odd_count = sum((1 for count in freq.values() if count % 2 != 0))
        return odd_count <= 1
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    letter_freq = {}
    for letter in letters:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1
    palindromes = set()
    for length in range(7, len(letters) + 1):
        if length % 2 == 0:
            current_freq = letter_freq.copy()
            remaining = length // 2
            half = []
            for letter, count in current_freq.items():
                pairs = count // 2
                half.extend([letter] * (pairs * 2))
                current_freq[letter] %= 2
                remaining -= pairs
                if remaining == 0:
                    break
            if remaining == 0:
                for arrangement in set(map(''.join, permutations(half))):
                    palindrome = arrangement + arrangement[::-1]
                    palindromes.add(palindrome)
        else:
            current_freq = letter_freq.copy()
            if can_form_palindrome(current_freq):
                center_letter = next((letter for letter, count in current_freq.items() if count % 2 != 0), next(iter(current_freq)))
                half_length = (length - 1) // 2
                current_freq[center_letter] -= 1
                current_freq = {k: v for k, v in current_freq.items() if v > 0}
                half = []
                remaining = half_length
                for letter, count in current_freq.items():
                    pairs = count // 2
                    half.extend([letter] * (pairs * 2))
                    current_freq[letter] %= 2
                    remaining -= pairs
                    if remaining == 0:
                        break
                if remaining == 0:
                    for arrangement in set(map(''.join, permutations(half))):
                        palindrome = arrangement + center_letter + arrangement[::-1]
                        palindromes.add(palindrome)
    return palindromes