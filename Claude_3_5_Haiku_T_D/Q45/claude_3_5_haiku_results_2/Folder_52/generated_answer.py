from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            test_palindrome = ''.join(perm)
            reverse_palindrome = test_palindrome[::-1]
            if test_palindrome == reverse_palindrome:
                palindrome_set.add(test_palindrome)
    return palindrome_set