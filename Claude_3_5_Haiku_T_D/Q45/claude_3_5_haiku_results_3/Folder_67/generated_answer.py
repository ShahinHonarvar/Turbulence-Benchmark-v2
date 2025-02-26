from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    palindrome_set = set()
    for r in range(len(letters), 0, -1):
        for perm in set(permutations(letters, r)):
            for p in [''.join(p), ''.join(p[::-1])]:
                if len(p) >= 5 and p == p[::-1]:
                    palindrome_set.add(p)
    return palindrome_set