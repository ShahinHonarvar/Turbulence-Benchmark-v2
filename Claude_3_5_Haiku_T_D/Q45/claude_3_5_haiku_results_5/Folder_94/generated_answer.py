from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    letters = [char.lower() for char in s[3:5] if char.isalpha()]
    if len(letters) < 3:
        return set()

    def can_form_palindrome(letter_counts):
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            letter_counts = {}
            for letter in perm:
                letter_counts[letter] = letter_counts.get(letter, 0) + 1
            if can_form_palindrome(letter_counts):
                possible_palindrome = list(perm)
                if length % 2 == 0:
                    palindrome = possible_palindrome + possible_palindrome[::-1]
                else:
                    odd_letter = [letter for letter, count in letter_counts.items() if count % 2 != 0][0]
                    remaining_letters = [letter for letter in possible_palindrome if letter != odd_letter]
                    palindrome = remaining_letters + [odd_letter] + remaining_letters[::-1]
                palindrome_set.add(''.join(palindrome))
    return palindrome_set