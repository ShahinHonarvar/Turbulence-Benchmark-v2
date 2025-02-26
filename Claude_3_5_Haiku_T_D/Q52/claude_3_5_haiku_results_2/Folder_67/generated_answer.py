def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    n = len(s)
    for start in range(n - 41):
        for end in range(start + 42, n + 1):
            substring = s[start:end]
            if len(substring) == 42 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes