def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 84, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= 84 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes