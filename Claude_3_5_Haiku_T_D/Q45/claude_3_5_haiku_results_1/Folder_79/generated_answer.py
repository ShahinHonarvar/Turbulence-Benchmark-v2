from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1] and len(candidate) >= 3:
                    palindrome_set.add(candidate)
    return palindrome_set