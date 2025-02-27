def filter_chars(text):
    chars_to_remove = []
    for i in range(44, 59):
        if i >= len(text):
            break
        if text[i] > '5' and text[i] < 'C':
            chars_to_remove.append(text[i])
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text