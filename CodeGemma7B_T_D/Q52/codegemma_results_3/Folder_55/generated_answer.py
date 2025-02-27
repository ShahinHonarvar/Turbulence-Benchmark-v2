def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 96):
        for j in range(i + 97, len(string) + 1):
            substring = string[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes