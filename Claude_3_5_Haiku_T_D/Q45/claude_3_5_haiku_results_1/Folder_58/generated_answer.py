from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindrome_set = set()
    for r in range(6, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            if r % 2 == 0:
                for half in set(permutations(perm[:r // 2])):
                    candidate = half + tuple(reversed(half))
                    if len(candidate) >= 6:
                        palindrome_set.add(''.join(candidate))
            else:
                for mid in set(perm[:1]):
                    for half in set(permutations(perm[1:r // 2 + 1])):
                        candidate = half + (mid,) + tuple(reversed(half))
                        if len(candidate) >= 6:
                            palindrome_set.add(''.join(candidate))
    return palindrome_set