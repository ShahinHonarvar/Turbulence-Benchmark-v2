def palindrome_of_length_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    n = 475
    palindromes = set()
    if len(string) < n:
        return palindromes
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes