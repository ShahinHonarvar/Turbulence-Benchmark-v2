from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    unique_palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if is_palindrome_possible(perm):
                unique_palindromes.add(''.join(perm))
    return unique_palindromes

def is_palindrome_possible(perm):
    return perm == perm[::-1]