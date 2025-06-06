def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i, length):
            substring = s[i:j + 1]
            if len(substring) >= 137 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes