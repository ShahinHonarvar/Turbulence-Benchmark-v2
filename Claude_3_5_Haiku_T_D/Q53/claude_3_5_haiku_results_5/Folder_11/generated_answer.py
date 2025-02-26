def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for start in range(len(string)):
        for end in range(start + 54, len(string) + 1):
            substring = string[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes