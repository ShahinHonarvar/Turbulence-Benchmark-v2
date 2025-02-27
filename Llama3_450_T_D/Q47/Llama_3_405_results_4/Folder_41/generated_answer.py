def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    return set((i for i in (s[j:j + k] for j in range(len(s)) for k in range(3, 5)) if i == i[::-1] and i.isalpha()))