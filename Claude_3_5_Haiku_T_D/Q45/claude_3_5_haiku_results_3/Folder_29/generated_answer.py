from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for p in list(map(''.join, [perm[i:] + perm[:i][::-1] for i in range(len(perm))])):
                if p == p[::-1] and len(p) >= 6:
                    palindrome_set.add(p)
    return palindrome_set