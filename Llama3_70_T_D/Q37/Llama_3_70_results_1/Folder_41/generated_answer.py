def filter_chars(s):
    filtered_chars = []
    for char in s:
        if not (26 <= ord(char) <= 64 and 'V' <= char <= 'o'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)