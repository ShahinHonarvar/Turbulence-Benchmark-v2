from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                candidate = perm[i:j] + perm[i:j][::-1]
                if len(candidate) >= 4 and candidate == candidate[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set