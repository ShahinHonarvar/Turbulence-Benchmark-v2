def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for start in range(length - 474):
        for end in range(start + 475, length + 1):
            substring = s[start:end]
            if len(substring) == 475 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes