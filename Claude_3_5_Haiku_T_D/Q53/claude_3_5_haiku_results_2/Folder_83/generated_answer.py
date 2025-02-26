def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(len(s), 59, -1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if len(substring) >= 60 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes