def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    n = 27
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes