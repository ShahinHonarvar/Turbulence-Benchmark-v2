def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    return set((i for l in range(13, 50) for i in (s[j:j + l] for j in range(len(s) - l + 1)) if i.isalpha() and i == i[::-1]))