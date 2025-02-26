def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for start in range(len(string) - 278):
        for end in range(start + 279, len(string) + 1):
            substring = string[start:end]
            if len(substring) == 279 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes