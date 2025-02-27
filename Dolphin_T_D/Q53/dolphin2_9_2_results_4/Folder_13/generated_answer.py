def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for length in range(52, 0, -1):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes