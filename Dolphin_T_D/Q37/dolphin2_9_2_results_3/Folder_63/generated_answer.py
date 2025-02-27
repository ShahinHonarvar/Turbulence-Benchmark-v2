def filter_chars(s):
    chars = set()
    for i in range(42, 93):
        c = s[i]
        if c >= '/' and c <= 'a':
            chars.add(c)
    result = ''
    for c in s:
        if c not in chars:
            result += c
    return result