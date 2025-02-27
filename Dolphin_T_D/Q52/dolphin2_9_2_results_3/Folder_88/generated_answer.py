def palindrome_of_length_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string) - 12):
        substring = string[i:i + 13]
        if substring == substring[::-1] and all((letter.isalpha() for letter in substring)):
            result.add(substring)
    return result