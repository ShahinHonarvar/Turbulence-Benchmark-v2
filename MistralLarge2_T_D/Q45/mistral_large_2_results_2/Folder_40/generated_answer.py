from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters_lower = ''.join(letters).lower()
    palindromes = set()
    for length in range(7, len(letters_lower) + 1):
        for perm in permutations(letters_lower, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes