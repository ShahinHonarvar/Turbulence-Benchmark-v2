def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 26):
        substring = string[i:i + 27]
        if len(substring) == 27 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes