def filter_chars(text):
    chars_to_remove = set()
    for i in range(513, 878):
        if '?' <= text[i] <= 'n':
            chars_to_remove.add(text[i])
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text