def palindrome_of_length_at_least_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 3, length):
            substring = string[i:j + 1]
            if substring.lower() == substring[::-1].lower() and len(substring) >= 34:
                palindromes.add(substring)
    return palindromes