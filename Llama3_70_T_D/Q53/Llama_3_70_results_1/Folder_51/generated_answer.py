def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(63, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes