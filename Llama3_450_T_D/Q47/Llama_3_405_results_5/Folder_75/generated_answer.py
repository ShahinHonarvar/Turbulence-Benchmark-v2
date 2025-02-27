def palindromes_of_specific_lengths(s):
    s = s[31:75].lower()
    return set((i for i in (s[j:j + k] for j in range(len(s)) for k in range(23, 40)) if i.isalpha() and i == i[::-1]))