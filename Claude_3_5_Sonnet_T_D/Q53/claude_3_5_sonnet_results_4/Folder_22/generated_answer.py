def palindrome_of_length_at_least_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    n = 97
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n - 1, len(string)):
            substring = string[i:j + 1]
            if len(substring) >= n and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes