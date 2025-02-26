def palindrome_of_length_n(string):
    n = 173
    palindromes = set()
    if len(string) < n:
        return palindromes
    string = string.lower()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes