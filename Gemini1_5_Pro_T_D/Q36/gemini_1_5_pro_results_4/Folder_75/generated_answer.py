def filter_chars(text):
    chars_to_remove = []
    for i in range(46, 74):
        if i >= len(text):
            break
        if text[i] > '&' and text[i] < 'M':
            chars_to_remove.append(text[i])
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text