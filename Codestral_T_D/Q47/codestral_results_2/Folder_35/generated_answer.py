def palindromes_of_specific_lengths(s):
    s = s[34:91]
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return {s[i:j] for i in range(len(s)) for j in range(i + 14, i + 40) if s[i:j] == s[i:j][::-1]}