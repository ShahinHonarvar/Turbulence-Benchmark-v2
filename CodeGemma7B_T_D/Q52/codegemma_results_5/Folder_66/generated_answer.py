def palindrome_of_length_n(string):
    letters = set(string.lower())
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 25, len(string) + 1):
            substring = string[i:j]
            if substring in palindromes:
                continue
            if substring == substring[::-1] and set(substring) <= letters:
                palindromes.add(substring)
    return palindromes