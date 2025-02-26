def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(43, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes