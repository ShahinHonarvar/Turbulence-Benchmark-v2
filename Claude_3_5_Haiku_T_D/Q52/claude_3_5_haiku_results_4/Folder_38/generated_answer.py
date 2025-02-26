def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 37):
        substring = string[i:i + 38]
        if len(substring) == 38 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes