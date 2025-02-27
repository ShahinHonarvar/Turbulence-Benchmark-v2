def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for length in range(149, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes