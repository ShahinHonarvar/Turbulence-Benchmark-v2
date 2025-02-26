def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    n = 52
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if len(substring) >= n and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes