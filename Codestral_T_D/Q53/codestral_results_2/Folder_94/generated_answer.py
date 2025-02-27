def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 41, length + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes