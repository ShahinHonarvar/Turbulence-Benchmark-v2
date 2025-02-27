def palindrome_of_length_n(string):
    n = 80
    palindromes = set()
    length = len(string)
    string = string.lower()
    for i in range(length - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes