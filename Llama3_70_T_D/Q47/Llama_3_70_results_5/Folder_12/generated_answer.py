def palindromes_of_specific_lengths(s):
    s = s[62:89].lower()
    return {s[i:i + j] for i in range(len(s)) for j in range(18, 22) if i + j <= len(s) and s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha()}