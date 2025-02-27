def palindrome_of_length_n(string, length=18):
    palindromes = set()
    string = ''.join((c.lower() for c in string if c.isalpha()))
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes