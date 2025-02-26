def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 406):
        substring = s[start:start + 407]
        if len(substring) == 407 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes