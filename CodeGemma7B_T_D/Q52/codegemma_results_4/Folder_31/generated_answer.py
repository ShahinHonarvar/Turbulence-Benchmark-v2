def palindrome_of_length_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result