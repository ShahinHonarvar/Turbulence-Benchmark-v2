def filter_chars(text):
    for i in range(2, 4):
        a = ord(text[i])
        if a >= ord('5') and a <= ord('_'):
            text = text.replace(chr(a), '')
    return text