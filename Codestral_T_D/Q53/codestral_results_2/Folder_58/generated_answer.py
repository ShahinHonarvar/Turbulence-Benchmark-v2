def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for length in range(147, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes