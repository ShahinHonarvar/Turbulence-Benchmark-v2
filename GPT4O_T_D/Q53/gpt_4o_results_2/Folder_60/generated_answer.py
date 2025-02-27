def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    palindromes = set()
    min_length = 80
    for i in range(n):
        for j in range(i + min_length, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes