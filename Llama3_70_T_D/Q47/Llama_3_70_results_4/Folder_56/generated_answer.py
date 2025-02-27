def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 3, min(i + 8, len(s) + 1)) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}
    return palindromes