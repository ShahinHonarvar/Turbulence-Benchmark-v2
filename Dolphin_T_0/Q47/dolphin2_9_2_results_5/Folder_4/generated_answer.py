def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s[11:93] if c.isalpha())).lower()
    return set((s[i:j] for i in range(s.rindex(s[-17:])) for j in range(i + 17, s.index(s[66:]) + 1) if s[i:j - 1] == ''.join(reversed(s[i:j - 1])) and len(s[i:j - 1]) in range(17, 67)))