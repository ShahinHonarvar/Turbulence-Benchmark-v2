def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 26):
        substring = string[i:i + 27]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes