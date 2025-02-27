def palindromes_of_specific_lengths(s):
    return set((s[i:j] for i in range(13, 100) for j in range(i + 26, min(i + 30, 100)) if s[i:j].lower() == s[i:j].lower()[::-1] and s[i:j].isalpha()))