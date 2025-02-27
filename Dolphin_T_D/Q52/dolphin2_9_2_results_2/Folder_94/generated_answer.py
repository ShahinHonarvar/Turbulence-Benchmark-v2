def palindrome_of_length_n(string):
    string = string.lower()
    n = 93
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) == n:
                palindromes.add(substring)
    return palindromes