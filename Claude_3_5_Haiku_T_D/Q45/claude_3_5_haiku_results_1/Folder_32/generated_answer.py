from itertools import permutations

def palindromes_between_indices(s):
    letters_in_range = [c.lower() for c in s[1:8] if c.isalpha()]
    if len(letters_in_range) < 5:
        return set()
    palindrome_set = set()
    for r in range(5, len(letters_in_range) + 1):
        for perm in set(permutations(letters_in_range, r)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if len(candidate) >= 5 and candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set