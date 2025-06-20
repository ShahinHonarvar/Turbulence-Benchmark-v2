def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 63):
        substring = string[i:i + 64]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes