def filter_chars(text):
    to_remove = []
    for i in range(56, 80):
        if i < len(text) and 'S' < text[i] < 's':
            to_remove.append(text[i])
    for char in to_remove:
        text = text.replace(char, '')
    return text