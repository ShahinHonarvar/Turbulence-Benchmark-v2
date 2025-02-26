def palindrome_of_length_at_least_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 45, length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes