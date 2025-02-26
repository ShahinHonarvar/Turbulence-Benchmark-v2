def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for start in range(len(string) - 205):
        for end in range(start + 206, len(string) + 1):
            substring = string[start:end]
            if len(substring) == 206 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes