def filter_chars(txt):
    V = ord('V')
    j = ord('j')
    result = ''
    for i, char in enumerate(txt):
        if i < 69 or i >= 97:
            result += char
    for i, char in enumerate(txt):
        if V <= ord(char) < j:
            txt = txt[:i] + txt[i + 1:]
    return result