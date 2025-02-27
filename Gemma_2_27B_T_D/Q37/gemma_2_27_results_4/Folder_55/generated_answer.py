def filter_chars(text):
    chars_to_remove = set()
    for i in range(1, 6):
        if i < len(text) and text[i] >= '$' and (text[i] <= ';'):
            chars_to_remove.add(text[i])
    result = ''.join([char for char in text if char not in chars_to_remove])
    return result