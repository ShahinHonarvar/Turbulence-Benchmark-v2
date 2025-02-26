def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 185):
        for end in range(start + 186, len(s) + 1):
            substring = s[start:end]
            if len(substring) == 186 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes