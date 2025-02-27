def palindrome_of_length_n(string):
    string = string.lower()
    length = 186
    palindromes = set()
    for i in range(len(string) - length + 1):
        for j in range(i + length):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) == length:
                palindromes.add(substring)
    return palindromes