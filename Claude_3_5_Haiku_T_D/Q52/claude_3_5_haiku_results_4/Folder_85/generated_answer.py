def palindrome_of_length_n(string):
    string = string.lower()
    n = 46
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == n and substring.isalpha() and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes