def palindromes_between_indices(s):
    s = s[3:7].lower()
    return set((s[i:j] for i in range(len(s)) for j in range(i + 4, len(s) + 1) if s[i:j] == s[i:j][::-1]))