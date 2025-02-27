def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 2, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 24 and substring.isalpha():
                palindromes.add(substring)
    return palindromes