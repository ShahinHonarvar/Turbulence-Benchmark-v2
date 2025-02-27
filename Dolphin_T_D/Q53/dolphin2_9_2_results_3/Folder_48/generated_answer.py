def palindrome_of_length_at_least_n(string):
    string = string.lower()
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = string[i:j]
            if len(substring) >= 150 and substring == substring[::-1]:
                if all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes