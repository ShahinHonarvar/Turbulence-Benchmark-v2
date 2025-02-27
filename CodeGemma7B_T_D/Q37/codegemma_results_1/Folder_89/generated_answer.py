def filter_chars(text):
    for i in range(11, 32):
        while i in range(len(text)):
            if text[i] in ''.join((chr(i) for i in range(33, 64))):
                text = text[:i] + text[i + 1:]
                continue
            i += 1
    return text