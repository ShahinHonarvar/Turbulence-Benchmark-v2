def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for length in range(100, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = ''.join(filter(str.isalpha, s[i:i + length]))
            if substring == substring[::-1] and len(substring) >= 100:
                palindromes.add(substring)
    return palindromes