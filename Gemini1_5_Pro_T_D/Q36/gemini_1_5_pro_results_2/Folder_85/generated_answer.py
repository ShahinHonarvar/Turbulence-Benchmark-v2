def filter_chars(text):
    chars_to_remove = set()
    for i in range(55, 80):
        if i < len(text) and 'S' < text[i] < 's':
            chars_to_remove.add(text[i])
    result = []
    for char in text:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)