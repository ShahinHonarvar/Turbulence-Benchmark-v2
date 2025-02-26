def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 76):
        substring = string[i:i + 77]
        if len(substring) == 77 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes