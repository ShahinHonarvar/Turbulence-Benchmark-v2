def palindrome_of_length_n(string):
    string = string.upper()
    palindromes = set()
    for i in range(len(string) - 68):
        for j in range(i + 69, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes