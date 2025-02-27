def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if len(s) - i >= 289:
            substring = s[i:i + 289]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes