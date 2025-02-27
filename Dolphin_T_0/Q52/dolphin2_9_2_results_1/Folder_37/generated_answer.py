def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 83):
        substring = string[i:i + 84]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes