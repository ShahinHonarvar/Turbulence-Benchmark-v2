def filter_chars(text):
    filtered = []
    for char in text:
        if 86 < ord(char) < 93:
            if 'E' < char < '~':
                filtered.append(char)
    result = ''.join(filtered)
    return result