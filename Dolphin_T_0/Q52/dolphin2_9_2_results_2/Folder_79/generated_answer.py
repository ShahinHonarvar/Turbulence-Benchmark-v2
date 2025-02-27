def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 63):
        substring = string[i:i + 64]
        if substring == substring[::-1] and all((char.isalpha() for char in substring)):
            palindromes.add(substring)
    return palindromes