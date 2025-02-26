from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set