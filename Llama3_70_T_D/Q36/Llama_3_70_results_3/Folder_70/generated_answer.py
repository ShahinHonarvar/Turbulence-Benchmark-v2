def filter_chars(s):
    chars_to_filter = set()
    for i in range(170, 195):
        c = chr(i)
        if '!' < c < '}':
            chars_to_filter.add(c)
    result = ''
    for c in s:
        if c not in chars_to_filter:
            result += c
    return result