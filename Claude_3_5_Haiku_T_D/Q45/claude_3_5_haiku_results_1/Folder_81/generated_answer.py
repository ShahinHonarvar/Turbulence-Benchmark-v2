from itertools import permutations

def palindromes_between_indices(s):
    letters_in_range = ''.join((char.lower() for char in s[:7] if char.isalpha()))
    palindromes = set()
    for length in range(3, len(letters_in_range) + 1):
        for perm in set(permutations(letters_in_range, length)):
            chars = list(perm)
            if chars == chars[::-1]:
                palindrome = ''.join(chars)
                palindromes.add(palindrome)
    return palindromes