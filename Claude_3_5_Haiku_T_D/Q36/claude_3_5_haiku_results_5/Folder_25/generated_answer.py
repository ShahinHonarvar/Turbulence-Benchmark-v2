def filter_chars(text):
    if len(text) <= 38:
        return text
    chars_to_remove = set()
    for i in range(25, 37):
        if 'A' < text[i] < 'h':
            chars_to_remove.add(text[i])
    result = ''.join((char for char in text if char not in chars_to_remove))
    return result