def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 6):
        substring = string[i:i + 7]
        if len(substring) == 7 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes