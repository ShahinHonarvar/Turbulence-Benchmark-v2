def filter_chars(text):
    filtered_text = []
    for char in text:
        if not (61 < ord(char) < 88 and char > '%' and (char < 'q')):
            filtered_text.append(char)
    return ''.join(filtered_text)