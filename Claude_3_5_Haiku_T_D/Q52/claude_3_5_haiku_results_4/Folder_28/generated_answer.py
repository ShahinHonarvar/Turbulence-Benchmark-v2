def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 42):
        substring = s[i:i + 43]
        if len(substring) == 43 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes