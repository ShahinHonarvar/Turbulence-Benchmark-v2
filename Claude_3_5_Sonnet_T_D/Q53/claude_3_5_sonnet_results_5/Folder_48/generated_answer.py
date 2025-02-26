def palindrome_of_length_at_least_n(string):
    string = ''.join(filter(str.isalpha, string.lower()))
    n = 150
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes