def palindrome_of_length_n(string):
    string = string.lower()
    length = 9
    result = set()
    for i in range(len(string)):
        for j in range(i + length, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                result.add(substring)
    return result