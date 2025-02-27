def palindrome_of_length_at_least_n(string):
    palindromes = set()
    length = len(string)
    string = string.lower()
    for i in range(length):
        for j in range(i + 9, length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes