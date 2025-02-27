def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 77, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 78:
                palindromes.add(substring)
    return palindromes