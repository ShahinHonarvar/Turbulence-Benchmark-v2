def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 75):
        substring = string[i:i + 76]
        if len(substring) == 76 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes