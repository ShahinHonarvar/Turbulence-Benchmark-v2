def filter_chars(text):
    chars_to_remove = [text[i] for i in range(45, 57) if 'F' < text[i] < 'n']
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text