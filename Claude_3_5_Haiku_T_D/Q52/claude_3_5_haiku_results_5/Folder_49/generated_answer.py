def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 46):
        substring = s[i:i + 47]
        if len(substring) == 47 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes