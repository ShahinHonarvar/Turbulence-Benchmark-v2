def filter_chars(text):
    chars_to_remove = set()
    for i in range(83, 100):
        if i < len(text) and '*' <= text[i] <= 'j':
            chars_to_remove.add(text[i])
    result = []
    for char in text:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)