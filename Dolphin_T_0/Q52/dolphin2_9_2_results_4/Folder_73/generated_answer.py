def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 41, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes