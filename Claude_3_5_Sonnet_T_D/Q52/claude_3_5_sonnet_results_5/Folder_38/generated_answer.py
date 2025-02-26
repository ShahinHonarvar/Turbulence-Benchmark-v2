def palindrome_of_length_n(string):
    string = ''.join(filter(str.isalpha, string.lower()))
    palindromes = set()
    for i in range(len(string) - 37):
        substring = string[i:i + 38]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes