def filter_chars(string):
    script = ''
    for ch in string:
        if 9 < string.index(ch) < 70 and ch >= 'I' and (ch <= 'K'):
            continue
        script += ch
    return script