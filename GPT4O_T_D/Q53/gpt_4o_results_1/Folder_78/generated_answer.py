def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 96, n + 1):
            substring = s[start:end]
            if substring == substring[::-1] and len(substring) >= 96:
                palindromes.add(substring)
    return palindromes