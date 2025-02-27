def palindrome_of_length_at_least_n(string):
    n = 112
    string = ''.join(filter(str.isalpha, string)).lower()
    palindromes = set()
    length = len(string)
    for start in range(length):
        for end in range(start + n, length + 1):
            substring = string[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes