def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        if i + 64 <= length:
            substring = s[i:i + 64]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes