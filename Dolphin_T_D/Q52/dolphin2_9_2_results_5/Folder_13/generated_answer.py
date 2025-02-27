def palindrome_of_length_n(string):
    string = string.replace(' ', '').lower()
    palindromes = set()
    for i in range(len(string) - 205):
        substring = string[i:i + 206]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes