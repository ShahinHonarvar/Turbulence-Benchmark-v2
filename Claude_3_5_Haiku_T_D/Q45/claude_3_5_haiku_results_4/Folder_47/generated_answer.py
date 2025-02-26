from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[3:8] if c.isalpha()))
    if len(letters) < 5:
        return set()
    palindrome_set = set()
    for length in range(5, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set