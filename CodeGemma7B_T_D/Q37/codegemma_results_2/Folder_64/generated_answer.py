def filter_chars(text):
    new_text = ''
    for i in range(1, 8):
        for char in text:
            if char >= 'L' and char <= 'a':
                text = text.replace(char, '')
    return text