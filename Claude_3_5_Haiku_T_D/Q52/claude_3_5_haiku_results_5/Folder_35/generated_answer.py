def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if len(substring) == 116 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes