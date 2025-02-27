def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string_length = len(string)
    palindromes = set()
    for i in range(string_length):
        for j in range(i + 63, string_length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes