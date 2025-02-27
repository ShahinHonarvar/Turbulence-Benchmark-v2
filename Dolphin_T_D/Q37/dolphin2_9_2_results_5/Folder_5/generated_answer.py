def filter_chars(s):
    re_s = ''
    for char in s:
        if not (24 <= s.index(char) <= 82 and '5' <= char <= '<'):
            re_s += char
    return re_s