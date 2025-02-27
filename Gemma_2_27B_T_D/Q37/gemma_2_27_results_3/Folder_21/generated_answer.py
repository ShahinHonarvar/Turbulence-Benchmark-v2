def filter_chars(text):
    for i in range(603, 760):
        for char in text:
            if i == text.find(char) and 'Q' <= char <= 'h':
                text = text.replace(char, '')
    return text