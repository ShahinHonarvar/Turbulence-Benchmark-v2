def filter_chars(text):
    filtered_text = ''
    for char in text:
        if not (20 <= ord(char) <= 32 and char >= 'f' and (char <= 'o')):
            filtered_text += char
    return filtered_text