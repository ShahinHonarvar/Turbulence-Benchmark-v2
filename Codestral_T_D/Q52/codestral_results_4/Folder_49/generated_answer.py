def palindrome_of_length_n(s):
    n = 47
    palindromes = {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n].lower() == s[i:i + n][::-1].lower() and s[i:i + n].isalpha()}
    return palindromes