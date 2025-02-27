def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[17:73]
    return {s[i:j] for i in range(len(s)) for j in range(i + 50, i + 52) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}