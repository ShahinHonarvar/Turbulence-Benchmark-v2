def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    return set((sub for i in range(len(s)) for sub in [s[i:i + j + 1] for j in range(20, 31)] if sub == sub[::-1] and sub.isalpha()))