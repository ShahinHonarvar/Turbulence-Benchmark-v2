def filter_chars(city_str):
    res = ''
    for ch in city_str:
        if not (72 <= ord(ch) <= 94 and ch >= '.' and (ch <= 'b')):
            res += ch
    return res