def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    return set((p for i in range(len(s)) for p in [s[i:i + j + 1] for j in range(51, 54) if s[i:i + j + 1] == s[i:i + j + 1][::-1] and p.isalpha()]))