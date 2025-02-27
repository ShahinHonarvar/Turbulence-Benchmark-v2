def filter_chars(txt):
    res = ''
    for c in txt:
        if not ('L' <= c <= 'a' and 1 <= txt.index(c) <= 7):
            res += c
    return res