def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(11, len(string) + 1):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes