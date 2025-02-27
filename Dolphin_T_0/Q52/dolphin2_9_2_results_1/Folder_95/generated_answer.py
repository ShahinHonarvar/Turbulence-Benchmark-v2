def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 86):
        substring = string[i:i + 87]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes