def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length):
            substring = s[i:j]
            if len(substring) == 40 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes