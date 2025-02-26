def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 47):
        substring = s[i:i + 48]
        if len(substring) == 48 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes