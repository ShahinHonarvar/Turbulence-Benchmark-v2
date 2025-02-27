def filter_chars(text):
    new_text = ''.join([c for c in text[11:46] if ord(c) > ord('!') and ord(c) < ord('A')])
    text = text[:11] + new_text + text[46:]
    return text