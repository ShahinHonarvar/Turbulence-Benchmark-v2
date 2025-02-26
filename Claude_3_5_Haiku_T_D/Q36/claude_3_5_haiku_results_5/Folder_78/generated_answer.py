def filter_chars(text):
    if len(text) <= 34:
        return text
    chars_to_remove = set()
    for i in range(30, 33):
        if '%' < text[i] < 'a':
            chars_to_remove.add(text[i])
    result = ''.join((char for char in text if char not in chars_to_remove))
    return result