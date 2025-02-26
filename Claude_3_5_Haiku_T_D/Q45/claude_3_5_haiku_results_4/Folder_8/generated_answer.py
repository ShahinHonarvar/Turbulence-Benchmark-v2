from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    palindrome_set = set()
    for length in range(5, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if len(candidate) >= 5 and candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set