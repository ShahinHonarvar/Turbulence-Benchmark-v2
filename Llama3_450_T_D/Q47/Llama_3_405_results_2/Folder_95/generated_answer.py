def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    return set((i for i in (s[j:j + k] for j in range(len(s)) for k in (20, 21) if j + k <= len(s)) if i == i[::-1] and i.isalpha()))