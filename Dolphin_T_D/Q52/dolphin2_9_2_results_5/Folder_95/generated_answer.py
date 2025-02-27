def palindrome_of_length_n(string):
    string = string.replace(' ', '').lower()
    n = 87
    palindromes = set()
    for i in range(len(string)):
        for j in range(0, i + n):
            substring = string[i:i + n]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes