def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for start in range(len(s)):
        for end in range(start + 7, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes