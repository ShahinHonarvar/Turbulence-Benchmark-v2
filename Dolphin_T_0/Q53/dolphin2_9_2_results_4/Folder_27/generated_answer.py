def palindrome_of_length_at_least_n(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 1, length):
            substring = string[i:j + 1]
            if all((char in english_letters for char in substring)) and len(substring) >= 100 and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes