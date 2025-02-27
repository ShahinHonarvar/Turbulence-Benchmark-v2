def filter_chars(text):
    for i in range(515, 539):
        for char in text:
            if ord(char) >= ord('+') and ord(char) <= ord('}') and (char in text):
                text = text.replace(char, '')
    return text