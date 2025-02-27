def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 93, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result