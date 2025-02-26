def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for start in range(len(string) - 20):
        substring = string[start:start + 21]
        if len(substring) == 21 and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes