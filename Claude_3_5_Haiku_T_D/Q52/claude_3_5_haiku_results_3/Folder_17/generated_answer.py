def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 288):
        for end in range(start + 289, n + 1):
            substring = s[start:end]
            if len(substring) == 289 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes