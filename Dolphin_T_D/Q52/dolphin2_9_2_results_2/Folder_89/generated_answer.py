def palindrome_of_length_n(string):
    string = string.lower()
    chars = 'abcdefghijklmnopqrstuvwxyz'
    n = 37
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1] and all((c in chars for c in substring)):
            palindromes.add(substring)
    return palindromes