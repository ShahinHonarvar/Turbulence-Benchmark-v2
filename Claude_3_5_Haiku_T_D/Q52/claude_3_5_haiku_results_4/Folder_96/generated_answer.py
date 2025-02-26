def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 82):
        substring = string[i:i + 83]
        if len(substring) == 83 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes