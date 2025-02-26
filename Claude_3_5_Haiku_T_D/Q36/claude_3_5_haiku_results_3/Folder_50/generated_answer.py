def filter_chars(text):
    chars_to_remove = set()
    for i in range(62, 88):
        if '%' < text[i] < 'q':
            chars_to_remove.add(text[i])
    result = ''.join((char for char in text if char not in chars_to_remove))
    return result