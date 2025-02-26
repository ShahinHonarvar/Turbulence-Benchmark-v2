def palindrome_of_length_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    length = len(string)
    palindromes = set()
    for i in range(length - 187):
        substring = string[i:i + 188]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes