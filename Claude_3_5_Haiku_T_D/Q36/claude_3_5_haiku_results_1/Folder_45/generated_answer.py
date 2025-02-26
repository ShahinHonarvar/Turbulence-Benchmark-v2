def filter_chars(text):
    if len(text) <= 87:
        return text
    chars_to_remove = set()
    for i in range(82, 86):
        if '!' < text[i] < 's':
            chars_to_remove.add(text[i])
    result = []
    for char in text:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)