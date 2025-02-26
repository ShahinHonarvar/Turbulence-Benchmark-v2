from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(7, len(perm) + 1):
            candidate = perm[:length]
            if len(candidate) % 2 == 0:
                half = len(candidate) // 2
                if list(candidate[:half]) == list(reversed(candidate[half:])):
                    palindromes.add(''.join(candidate))
            else:
                half = len(candidate) // 2
                if list(candidate[:half]) == list(reversed(candidate[half + 1:])):
                    palindromes.add(''.join(candidate))
    return palindromes