def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 80
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes