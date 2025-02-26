def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for start in range(len(string)):
        for end in range(start + 23, len(string) + 1):
            substring = string[start:end]
            if len(substring) >= 23 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes