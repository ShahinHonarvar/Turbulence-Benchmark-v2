def remove_repeat_chars(text):
    return ''.join(sorted(list(text[:36]) + list(text[52:]) + list(text[36:52]), key=text.index))