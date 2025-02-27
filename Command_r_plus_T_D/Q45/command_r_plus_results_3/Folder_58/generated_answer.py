def palindromes_between_indices(s):
    s = s[:7]
    s = ''.join(filter(str.isalpha, s)).lower()
    return set((word for word in s[i:] + s[:i] for i in range(len(s) + 1) if len(word) >= 6 and word == word[::-1]))