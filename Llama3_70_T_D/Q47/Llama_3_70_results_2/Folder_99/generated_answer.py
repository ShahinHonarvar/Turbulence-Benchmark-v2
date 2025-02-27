def palindromes_of_specific_lengths(s):
    s = s[127:289].lower()
    return set((w for i in range(len(s)) for w in [s[i:i + j] for j in range(119, 142) if s[i:i + j] == s[i:i + j][::-1] and w.isalpha()]))