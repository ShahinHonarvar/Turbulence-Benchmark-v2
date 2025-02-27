def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length - 3):
        substring = string[i:i + 4]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes