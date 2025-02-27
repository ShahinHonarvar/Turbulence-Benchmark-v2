def palindromes_between_indices(s):
    s = s[:7]
    s = ''.join(filter(str.isalpha, s)).lower()
    return set((w + w[::-1] for w in s if len(w) >= 3))