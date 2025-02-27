def palindromes_of_specific_lengths(s):
    return {w for w in [s[i:i + l] for l in range(3, 6) for i in range(6)] if w == w[::-1] and w.isalpha()}