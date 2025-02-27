def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 2, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 122:
                palindromes.add(substring)
    return palindromes