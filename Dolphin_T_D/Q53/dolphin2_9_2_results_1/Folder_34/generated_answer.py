def palindrome_of_length_at_least_n(string):
    string = string.lower()
    n = 68
    palindromes = set()
    for i in range(len(string) - n + 1):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes