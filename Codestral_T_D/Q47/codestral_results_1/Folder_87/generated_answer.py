def palindromes_of_specific_lengths(s):
    s = s[11:94].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 34, i + 55) if j <= len(s) and s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}