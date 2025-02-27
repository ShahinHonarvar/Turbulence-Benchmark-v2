def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        for _ in range(i + 6):
            string = string.lower()
            substring = string[i:i + 6]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes