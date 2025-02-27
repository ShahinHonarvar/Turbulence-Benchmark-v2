def palindrome_of_length_at_least_n(string):
    string = string.lower()
    n = 41
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + n - 1, length):
            substring = string[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes