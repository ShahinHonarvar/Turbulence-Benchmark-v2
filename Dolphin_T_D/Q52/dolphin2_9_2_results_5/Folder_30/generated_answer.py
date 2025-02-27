def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 93, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) == 94:
                palindromes.add(substring)
    return palindromes