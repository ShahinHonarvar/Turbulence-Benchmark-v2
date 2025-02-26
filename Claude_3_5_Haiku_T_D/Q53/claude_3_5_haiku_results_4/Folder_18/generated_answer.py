def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 62
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes