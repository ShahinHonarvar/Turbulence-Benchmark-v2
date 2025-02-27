def filter_chars(text):
    filtered_chars = ''
    for i in range(len(text)):
        if 29 <= i <= 79 and 'K' <= text[i] <= 'z':
            filtered_chars += text[i]
    result = ''
    for char in text:
        if char not in filtered_chars:
            result += char
    return result