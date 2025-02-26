def palindrome_of_length_n(s):
    s = s.lower()
    n = 100
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes