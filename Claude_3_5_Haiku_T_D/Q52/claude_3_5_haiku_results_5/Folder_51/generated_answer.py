def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for start in range(length - 72):
        substring = s[start:start + 73]
        if len(substring) == 73 and all((char.isalpha() for char in substring)):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes