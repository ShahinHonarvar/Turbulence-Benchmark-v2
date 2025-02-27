def filter_chars(txt):
    maxed = min(max(txt[1:7]), '^')
    for char in txt:
        if char > '3' and char != maxed:
            txt = txt.replace(char, '')
    return txt