def palindrome_of_length_n(string):
    string = string.lower()
    string = ''.join([c for c in string if c.isalpha()])
    length = 64
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes