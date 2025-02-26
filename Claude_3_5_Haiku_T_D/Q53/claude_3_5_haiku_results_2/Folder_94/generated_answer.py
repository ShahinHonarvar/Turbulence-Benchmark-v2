def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            substring = s[start:end]
            if len(substring) >= 41 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes