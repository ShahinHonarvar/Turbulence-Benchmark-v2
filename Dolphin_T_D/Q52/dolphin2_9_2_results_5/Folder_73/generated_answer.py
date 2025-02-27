def palindrome_of_length_n(string):
    string = string.lower()
    length = len(string)
    result = set()
    for i in range(length - 40):
        substring = string[i:i + 41]
        if substring == substring[::-1]:
            result.add(substring)
    return result