def palindromes_of_specific_lengths(s):
    s = s[15:90]
    return set((s[i:j + 1] for i in range(len(s) - 40) for j in range(i + 40, min(len(s), i + 73)) if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and s[i:j + 1].isalpha()))