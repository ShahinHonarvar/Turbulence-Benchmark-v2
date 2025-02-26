from collections import Counter

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:6] if char.isalpha()]
    palindromes = set()

    def can_form_palindrome(letter_counts):
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(letter_counts, current_palindrome='', length=0):
        if length == 5 or length == 6 or length == 7:
            if can_form_palindrome(letter_counts):
                mid_char = ''
                half_palindrome = []
                for letter, count in letter_counts.items():
                    if count % 2 != 0:
                        mid_char = letter
                    half_palindrome.extend([letter] * (count // 2))
                if mid_char:
                    full_palindrome = half_palindrome + [mid_char] + half_palindrome[::-1]
                else:
                    full_palindrome = half_palindrome + half_palindrome[::-1]
                palindrome_str = ''.join(full_palindrome)
                palindromes.add(palindrome_str)
        for letter, count in list(letter_counts.items()):
            if count > 0:
                letter_counts[letter] -= 2
                generate_palindromes(letter_counts, current_palindrome + letter, length + 2)
                letter_counts[letter] += 2
    letter_counts = Counter(letters)
    generate_palindromes(letter_counts)
    return palindromes