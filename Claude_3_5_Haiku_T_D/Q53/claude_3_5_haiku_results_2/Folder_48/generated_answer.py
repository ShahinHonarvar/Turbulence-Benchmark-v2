def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 150, n + 1):
            substring = s[i:j]
            if len(substring) >= 150 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes