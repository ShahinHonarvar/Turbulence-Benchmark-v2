def palindrome_of_length_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    n = 37
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes