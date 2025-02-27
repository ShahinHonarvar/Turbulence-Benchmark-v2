def palindrome_of_length_at_least_n(string):
    string = string.lower()
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 4, length):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes