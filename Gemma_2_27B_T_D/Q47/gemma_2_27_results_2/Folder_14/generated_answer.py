def palindromes_of_specific_lengths(s):
    return set((p for i in range(10, 75) for p in [s[i:i + l] for l in range(6, 9) if s[i:i + l] == s[i:i + l][::-1] and s[i:i + l].isalpha()]))