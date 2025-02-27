def palindrome_of_length_at_least_n(s):
    s = ''.join((ch.lower() for ch in s if ch.isalpha()))
    n = len(s)
    palindromes = set()
    for length in range(67, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes