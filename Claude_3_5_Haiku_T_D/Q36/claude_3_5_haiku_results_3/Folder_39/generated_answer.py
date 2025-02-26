def filter_chars(text):
    if len(text) <= 59:
        return text
    chars_to_remove = set()
    for i in range(44, 59):
        if '5' < text[i] < 'C':
            chars_to_remove.add(text[i])
    return ''.join((char for char in text if char not in chars_to_remove))