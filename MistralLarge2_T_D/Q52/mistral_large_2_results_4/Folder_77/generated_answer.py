def palindrome_of_length_n(string):
    n = 173
    palindromes = set()
    string = string.lower()
    length = len(string)
    for i in range(length - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes