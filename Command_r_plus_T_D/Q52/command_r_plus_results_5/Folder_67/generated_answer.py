def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, min(i + 43, length) + 1):
            substring = s[i:j]
            if len(substring) == 42 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes