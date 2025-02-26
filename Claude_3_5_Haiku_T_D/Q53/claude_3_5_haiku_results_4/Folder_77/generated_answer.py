def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(149, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes