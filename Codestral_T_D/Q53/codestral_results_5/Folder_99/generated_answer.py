def palindrome_of_length_at_least_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 15, length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes