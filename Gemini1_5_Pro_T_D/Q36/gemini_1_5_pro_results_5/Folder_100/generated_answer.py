def filter_chars(text):
    chars_to_remove = []
    for i in range(44, 69):
        if i >= len(text):
            break
        char = text[i]
        if char > 'B' and char < 'r':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text