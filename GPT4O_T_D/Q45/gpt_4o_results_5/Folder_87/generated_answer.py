from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    unique_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                unique_palindromes.add(''.join(perm))
    return unique_palindromes