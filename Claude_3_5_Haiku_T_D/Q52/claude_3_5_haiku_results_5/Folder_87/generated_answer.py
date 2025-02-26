def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 56):
        substring = string[i:i + 57]
        if len(substring) == 57 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes