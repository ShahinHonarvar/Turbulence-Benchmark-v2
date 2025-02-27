def filter_chars(text):
    for i in range(331, 713):
        char = text[i]
        if ord(char) > ord('M') and ord(char) < ord('_'):
            text = text.replace(char, '')
    return text