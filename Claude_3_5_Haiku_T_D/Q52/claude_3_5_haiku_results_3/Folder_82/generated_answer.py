def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 27):
        substring = string[i:i + 28]
        if len(substring) == 28 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes