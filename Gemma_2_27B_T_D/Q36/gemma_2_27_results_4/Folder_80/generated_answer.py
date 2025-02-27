def filter_chars(text):
    for i in range(54, 92):
        char = text[i]
        if ord(char) > ord('J') and ord(char) < ord('X'):
            text = text.replace(char, '')
    return text