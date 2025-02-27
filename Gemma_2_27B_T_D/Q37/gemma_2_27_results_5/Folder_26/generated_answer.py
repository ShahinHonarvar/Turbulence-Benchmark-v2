def filter_chars(text):
    for i in range(20, 63):
        char = text[i]
        if ord(char) >= ord('i') and ord(char) <= ord('k'):
            text = text.replace(char, '')
    return text