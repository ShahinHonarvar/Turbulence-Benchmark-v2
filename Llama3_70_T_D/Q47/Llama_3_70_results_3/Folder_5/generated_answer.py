def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    palindromes = {''.join(s[i:j + 1]) for i in range(len(s)) for j in range(i + 3, min(i + 6, len(s))) if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha()}
    return palindromes