def remove_repeat_chars(text):
    s = ''
    for c in text:
        if len(s) < 3 or len(s) > 9 or c not in s:
            s += c
    return s