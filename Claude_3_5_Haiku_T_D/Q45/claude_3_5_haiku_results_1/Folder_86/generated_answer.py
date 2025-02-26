from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for palindrome_candidate in [''.join(p) for p in [perm, perm[::-1]]]:
                if palindrome_candidate == palindrome_candidate[::-1]:
                    unique_palindromes.add(palindrome_candidate)
    return unique_palindromes