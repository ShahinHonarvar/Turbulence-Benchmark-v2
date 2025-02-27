def filter_chars(s):
    s = list(s)
    for idx, c in enumerate(s):
        if 15 <= idx < 85 and c > 'I' and (c < 'M'):
            s = [i for i in s if i != c]
    return ''.join(s)