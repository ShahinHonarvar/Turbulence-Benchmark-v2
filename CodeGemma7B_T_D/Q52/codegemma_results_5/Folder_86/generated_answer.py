def palindrome_of_length_n(text):
    result = set()
    length = 181
    text = text.lower()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if substring == substring[::-1]:
            result.add(substring)
    return result