def palindromes_of_specific_lengths(s):
    s = s[27:95].lower()
    return {substr for i in range(38, 50) for j in range(0, 95 - i + 1) if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha()}