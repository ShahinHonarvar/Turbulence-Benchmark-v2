def palindrome_of_length_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = set()
    for i in range(len(string) - 89):
        substring = string[i:i + 90]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes