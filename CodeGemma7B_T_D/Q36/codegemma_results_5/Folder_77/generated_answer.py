def filter_chars(text):
    filtered_text = ''
    for char in text:
        if not (221 < ord(char) < 419 and char > '-' and (char < 'v')):
            filtered_text += char
    return filtered_text