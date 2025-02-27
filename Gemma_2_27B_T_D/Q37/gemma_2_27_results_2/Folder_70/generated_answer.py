def filter_chars(text):
    remove_chars = set()
    for i in range(515, 539):
        if i < len(text) and '+' <= text[i] <= '}':
            remove_chars.add(text[i])
    result = ''.join((char for char in text if char not in remove_chars))
    return result