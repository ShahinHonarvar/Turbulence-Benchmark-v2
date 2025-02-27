def filter_chars(text):
    chars_to_remove = set()
    for i in range(2):
        if i < len(text) and '*' <= text[i] <= 's':
            chars_to_remove.add(text[i])
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text