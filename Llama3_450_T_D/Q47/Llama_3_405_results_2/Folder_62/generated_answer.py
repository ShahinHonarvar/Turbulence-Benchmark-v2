def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    palindromes = {s[i:i + j] for j in range(52, 57) for i in range(len(s) - j + 1) if s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha()}
    return palindromes