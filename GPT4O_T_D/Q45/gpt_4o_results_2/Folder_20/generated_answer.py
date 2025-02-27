from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    valid_chars = [c for c in s if c.isalpha()]
    permutations_set = set((''.join(p) for i in range(4, len(valid_chars) + 1) for p in permutations(valid_chars, i)))
    palindrome_set = set((p for p in permutations_set if p == p[::-1]))
    return palindrome_set