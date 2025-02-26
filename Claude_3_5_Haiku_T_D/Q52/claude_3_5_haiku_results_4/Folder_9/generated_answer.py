def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 71):
        substring = s[i:i + 72]
        if len(substring) == 72 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes