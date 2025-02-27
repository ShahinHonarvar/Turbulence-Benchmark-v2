def filter_chars(text):
    chars_to_remove = []
    for i in range(51, 91):
        if text[i] > 'A' and text[i] < 'Q':
            chars_to_remove.append(text[i])
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text