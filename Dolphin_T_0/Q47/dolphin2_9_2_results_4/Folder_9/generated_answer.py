def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    return set((s[i:j + 1] for i in range(300) for j in range(i + 49, min(i + 61, len(s))) if s[i:j + 1] == s[i:j + 1][::-1]))