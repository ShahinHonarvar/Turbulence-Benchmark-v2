from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = set(s[2:7].lower())
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes