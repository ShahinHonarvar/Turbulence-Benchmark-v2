def filter_chars(text):
    chars_to_remove = set()
    for i in range(40, 63):
        if text[i] > '7' and text[i] < 'H':
            chars_to_remove.add(text[i])
    result = []
    for char in text:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)