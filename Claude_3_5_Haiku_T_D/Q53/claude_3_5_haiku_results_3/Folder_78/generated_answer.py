def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for length in range(96, len(string) + 1):
        for start in range(len(string) - length + 1):
            substring = string[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes