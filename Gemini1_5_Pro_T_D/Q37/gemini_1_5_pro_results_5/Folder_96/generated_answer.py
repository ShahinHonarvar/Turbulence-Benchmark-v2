def filter_chars(text):
    filtered_chars = ''
    for i in range(86, 93):
        if i < len(text) and '!' <= text[i] <= 's':
            filtered_chars += text[i]
    result = ''
    for char in text:
        if char not in filtered_chars:
            result += char
    return result