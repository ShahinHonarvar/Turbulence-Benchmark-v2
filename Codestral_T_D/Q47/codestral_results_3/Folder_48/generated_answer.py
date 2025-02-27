def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 104, i + 121) if j <= len(s) and s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}