def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = 210
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(substring) == length and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes