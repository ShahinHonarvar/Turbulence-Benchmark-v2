def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 49, i + 52) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}
    return palindromes