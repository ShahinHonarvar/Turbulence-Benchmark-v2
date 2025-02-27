def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    return set((x for i in range(len(s)) for x in [s[i:i + j] for j in range(104, 121) if s[i:i + j] == s[i:i + j][::-1] and x.isalpha()]))