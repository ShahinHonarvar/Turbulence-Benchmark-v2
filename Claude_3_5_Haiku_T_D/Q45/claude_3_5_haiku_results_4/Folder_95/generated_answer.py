from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    letters = s[7:9]
    english_letters = ''.join((char.lower() for char in letters if char.isalpha()))
    if len(english_letters) < 3:
        return set()
    unique_palindromes = set()
    for perm_length in range(3, len(english_letters) + 1):
        for chars in set(permutations(english_letters, perm_length)):
            mid = len(chars) // 2
            left = chars[:mid]
            right = chars[mid + len(chars) % 2:][::-1]
            if left == right:
                palindrome = ''.join(chars)
                unique_palindromes.add(palindrome)
    return unique_palindromes