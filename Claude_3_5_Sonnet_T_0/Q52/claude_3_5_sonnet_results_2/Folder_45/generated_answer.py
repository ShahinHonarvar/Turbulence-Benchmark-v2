def palindrome_of_length_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    palindromes = set()
    for i in range(len(string) - 20):
        substring = string[i:i + 21]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes