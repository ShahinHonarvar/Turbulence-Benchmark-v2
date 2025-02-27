def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for length in range(31, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes