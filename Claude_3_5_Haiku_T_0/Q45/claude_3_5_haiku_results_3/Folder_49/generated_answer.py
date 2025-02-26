from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 2, len(perm) + 1):
                candidate = perm[i:j] + perm[i:j - 1][::-1]
                if len(candidate) >= 3 and candidate == candidate[::-1]:
                    palindrome_set.add(''.join(candidate))
    return palindrome_set