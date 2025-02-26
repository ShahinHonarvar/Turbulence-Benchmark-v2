from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:10] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if len(set(perm)) < length:
                continue
            candidate = ''.join(perm)
            if len(candidate) % 2 == 0:
                half = len(candidate) // 2
                if candidate[:half] == candidate[half:][::-1]:
                    palindromes.add(candidate)
            else:
                half = len(candidate) // 2
                if candidate[:half] == candidate[half + 1:][::-1]:
                    palindromes.add(candidate)
    return palindromes