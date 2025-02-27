def filter_chars(text):
    filtered_chars = ''
    for i in range(len(text)):
        if i in range(73, 75) and 'U' <= text[i] <= 'l':
            filtered_chars += text[i]
    for char in filtered_chars:
        text = text.replace(char, '')
    return text