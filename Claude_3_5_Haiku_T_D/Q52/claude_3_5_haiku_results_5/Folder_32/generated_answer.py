def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 112):
        substring = string[i:i + 113]
        if len(substring) == 113 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes