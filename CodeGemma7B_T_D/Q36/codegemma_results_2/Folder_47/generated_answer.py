def filter_chars(text):
    filtered_chars = []
    for char in text:
        if 45 < ord(char) < 57:
            if 'F' < char < 'n':
                continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)