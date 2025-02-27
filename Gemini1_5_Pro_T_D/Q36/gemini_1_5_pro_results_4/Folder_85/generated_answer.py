def filter_chars(text):
    chars_to_remove = []
    for i in range(55, 80):
        if i < len(text) and 'S' < text[i] < 's':
            chars_to_remove.append(text[i])
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text