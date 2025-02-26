from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:7] if char.isalpha()]
    if len(letters) < 6:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters, 6)):
        for arrangement in [perm, perm[::-1]]:
            candidate = ''.join(arrangement)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set