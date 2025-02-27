def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 39, length):
            substring = string[i:j + 1]
            if substring == ''.join(reversed(substring)) and len(substring) >= 40:
                palindromes.add(substring)
    return palindromes