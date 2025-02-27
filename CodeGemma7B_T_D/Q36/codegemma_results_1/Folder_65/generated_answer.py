def filter_chars(text):
    for i in range(58, 82):
        if ord(text[i]) > ord('F') and ord(text[i]) < ord('O'):
            text = text.replace(text[i], '')
    return text