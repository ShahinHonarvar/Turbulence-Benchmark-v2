def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 2):
        for j in range(i + 3, len(string) + 1):
            substring = string[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes