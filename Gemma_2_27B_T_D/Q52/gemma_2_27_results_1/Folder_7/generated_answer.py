def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 415):
        substring = text[i:i + 416].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result