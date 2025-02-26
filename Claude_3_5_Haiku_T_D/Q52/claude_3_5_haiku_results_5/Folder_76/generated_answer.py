def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for start in range(len(string) - 256):
        substring = string[start:start + 257]
        if len(substring) == 257 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes