def filter_chars(text):
    filtered_text = ''
    for char in text:
        if not (21 <= text.index(char) <= 43 and '+' <= char <= '8'):
            filtered_text += char
    return filtered_text