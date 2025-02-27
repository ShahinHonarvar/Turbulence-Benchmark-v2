def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = len(s)
    for length in range(147, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes