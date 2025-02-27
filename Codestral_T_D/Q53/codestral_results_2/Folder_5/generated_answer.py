def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(46, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes