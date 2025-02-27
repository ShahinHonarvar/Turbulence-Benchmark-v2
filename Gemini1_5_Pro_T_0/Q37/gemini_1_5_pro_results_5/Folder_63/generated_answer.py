def filter_chars(text):
    filtered_chars = ''
    for i in range(len(text)):
        if 42 <= i <= 92 and '/' <= text[i] <= 'a':
            filtered_chars += text[i]
    for char in filtered_chars:
        text = text.replace(char, '')
    return text