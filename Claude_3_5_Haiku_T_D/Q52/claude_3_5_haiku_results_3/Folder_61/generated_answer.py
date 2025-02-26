def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 73):
        substring = string[i:i + 74]
        if len(substring) == 74 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes