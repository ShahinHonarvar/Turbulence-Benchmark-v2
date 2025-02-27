def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    string_length = len(string)
    for i in range(string_length):
        for j in range(i + 146, string_length):
            substring = string[i:j + 1]
            if all((char in 'abcdefghijklmnopqrstuvwxyz' for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes