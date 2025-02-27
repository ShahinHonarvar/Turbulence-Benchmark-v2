def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 73, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) == 73:
                palindromes.add(substring)
    return palindromes