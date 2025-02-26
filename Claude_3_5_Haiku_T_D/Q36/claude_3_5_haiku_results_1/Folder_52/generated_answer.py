def filter_chars(text):
    chars_to_remove = set()
    for i in range(50, 56):
        if 'I' < text[i] < 'a':
            chars_to_remove.add(text[i])
    return ''.join((char for char in text if char not in chars_to_remove))