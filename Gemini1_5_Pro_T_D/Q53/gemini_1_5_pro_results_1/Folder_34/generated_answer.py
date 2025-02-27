def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 67):
        for j in range(i + 67, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower() and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes