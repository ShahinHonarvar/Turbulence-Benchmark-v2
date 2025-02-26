def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 68):
        for end in range(start + 69, n + 1):
            substring = s[start:end]
            if len(substring) == 69 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes