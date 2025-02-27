def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(34, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes