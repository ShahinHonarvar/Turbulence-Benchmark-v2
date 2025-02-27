def palindromes_of_specific_lengths(s):
    s = s[11:94].lower()
    return set((i for l in range(34, 55) for i in (s[j:j + l] for j in range(len(s) - l + 1)) if i == i[::-1] and i.isalpha()))