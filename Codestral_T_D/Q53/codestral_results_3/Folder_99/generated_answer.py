def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    length = len(string)
    for start in range(length):
        for end in range(start + 115, length + 1):
            substring = string[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes