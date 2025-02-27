def palindrome_of_length_n(string):
    string = string.lower()
    length = 206
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + length, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes