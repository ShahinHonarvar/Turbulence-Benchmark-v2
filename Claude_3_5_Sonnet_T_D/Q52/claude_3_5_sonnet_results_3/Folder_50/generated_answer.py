def palindrome_of_length_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    palindromes = set()
    length = len(string)
    for i in range(length - 39):
        substring = string[i:i + 40]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes