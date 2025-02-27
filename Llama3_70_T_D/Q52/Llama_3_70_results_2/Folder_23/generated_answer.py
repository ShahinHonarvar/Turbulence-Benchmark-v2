def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 68):
        substring = string[i:i + 69]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes