def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if len(substring) == 10 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes