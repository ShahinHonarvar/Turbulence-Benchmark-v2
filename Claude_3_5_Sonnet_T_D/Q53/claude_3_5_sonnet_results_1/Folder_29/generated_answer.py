def palindrome_of_length_at_least_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    n = 78
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n - 1, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes