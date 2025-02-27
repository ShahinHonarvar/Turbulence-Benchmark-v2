def palindromes_of_specific_lengths(s):
    s = s[:10].lower()
    return set((sub for i in range(1, 10) for sub in [s[i:i + j] for j in range(3, 8)] if sub == sub[::-1] and sub.isalpha()))