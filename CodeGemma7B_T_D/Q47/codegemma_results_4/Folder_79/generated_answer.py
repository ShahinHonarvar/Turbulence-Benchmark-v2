def palindromes_of_specific_lengths(s):
    return set((x for x in (s[i:i + n] for i in range(1, 9) for n in range(3, 5)) if x.isalpha() and x == x[::-1]))