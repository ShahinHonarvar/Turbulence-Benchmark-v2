def filter_chars(text):
    for i in range(2):
        for char in text:
            if ord(char) >= ord('*') and ord(char) <= ord('s'):
                text = text.replace(char, '')
    return text