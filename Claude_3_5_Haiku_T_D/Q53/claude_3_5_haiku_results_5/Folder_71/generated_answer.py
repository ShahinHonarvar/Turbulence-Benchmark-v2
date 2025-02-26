def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if len(substring) >= 87 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes