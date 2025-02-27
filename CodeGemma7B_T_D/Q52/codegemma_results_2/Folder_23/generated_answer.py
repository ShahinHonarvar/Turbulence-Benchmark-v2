def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string) - 68):
        for j in range(i + 1, len(string) - 68 + 1):
            substring = string[i:j]
            if substring == substring[::-1].lower():
                result.add(substring)
    return result