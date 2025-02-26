def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 3):
        substring = string[i:i + 4]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes