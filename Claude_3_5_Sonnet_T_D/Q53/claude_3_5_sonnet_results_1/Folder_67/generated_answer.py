def palindrome_of_length_at_least_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    n = len(string)
    palindromes = set()
    for i in range(n):
        for j in range(i + 25, n + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes