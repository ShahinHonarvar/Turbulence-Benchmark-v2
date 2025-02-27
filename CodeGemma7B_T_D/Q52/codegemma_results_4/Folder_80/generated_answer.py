def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1].lower()
            if substring == substring[::-1] and len(substring) == 276:
                result.add(substring)
    return result