def palindrome_of_length_at_least_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = set()
    n = len(string)
    for i in range(n):
        for j in range(i + 30, n + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes