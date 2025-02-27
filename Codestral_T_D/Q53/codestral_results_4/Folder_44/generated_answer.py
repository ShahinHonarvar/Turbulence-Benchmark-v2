def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 89
    length = len(string)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes