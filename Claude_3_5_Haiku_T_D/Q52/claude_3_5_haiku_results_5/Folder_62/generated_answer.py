def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    length = 188
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if len(substring) == length and substring == substring[::-1]:
            if all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes