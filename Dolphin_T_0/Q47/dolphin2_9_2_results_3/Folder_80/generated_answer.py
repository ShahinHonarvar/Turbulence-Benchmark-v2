def palindromes_of_specific_lengths(s):
    s = s[34:89].lower()
    return {s[i:i + n] for i in range(len(s)) for n in range(24, 34) if s[i:i + n] == s[i:i + n][::-1] and s[i:i + n].isalpha()}