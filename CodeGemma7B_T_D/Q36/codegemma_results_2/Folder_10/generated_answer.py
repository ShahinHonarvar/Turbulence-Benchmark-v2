def filter_chars(text):
    output = ''
    valid_chars = set((c for c in text if 35 < ord(c) < 60 and ord(c) > ord('!') and (ord(c) < ord('B'))))
    for char in text:
        if char not in valid_chars:
            output += char
    return output