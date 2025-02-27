def filter_chars(text):
    for i in range(323, 526):
        char = text[i]
        if ord(char) > ord(')') and ord(char) < ord('O'):
            text = text.replace(char, '')
    return text