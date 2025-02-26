def filter_chars(text):
    chars_to_remove = set()
    for i in range(35, 52):
        if i < len(text):
            char = text[i]
            if 'H' <= char <= 's':
                chars_to_remove.add(char)
    return ''.join((char for char in text if char not in chars_to_remove))