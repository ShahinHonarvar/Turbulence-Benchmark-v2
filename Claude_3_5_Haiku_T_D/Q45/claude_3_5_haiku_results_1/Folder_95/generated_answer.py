from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                if list(arrangement) == list(arrangement)[::-1]:
                    palindrome_set.add(''.join(arrangement))
    return palindrome_set