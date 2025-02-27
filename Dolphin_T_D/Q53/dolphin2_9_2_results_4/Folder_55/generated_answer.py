def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for length in range(83, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes