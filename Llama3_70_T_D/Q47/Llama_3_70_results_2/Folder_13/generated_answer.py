def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    return set((t for t in [s[i + j:i - j + 1] for j in range(1, 4) for i in range(28 - j, 43 + j)] if t == t[::-1] and t.isalpha()))