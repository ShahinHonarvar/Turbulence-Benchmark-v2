def filter_chars(text):
    filtered_text = ''
    for char in text:
        if not (text.index(char) >= 37 and text.index(char) <= 56 and (char >= '6') and (char <= '_')):
            filtered_text += char
    return filtered_text