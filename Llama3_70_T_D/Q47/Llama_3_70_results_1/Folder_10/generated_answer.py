def palindromes_of_specific_lengths(s):
    s = s[16:61].lower()
    return set((s[i:j] for i in range(len(s)) for j in range(i + 16, min(i + 40, len(s) + 1)) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()))