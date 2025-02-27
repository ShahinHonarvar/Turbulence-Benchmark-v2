def filter_chars(s):
    chars = [c for c in s if c < 'l' or c > 't']
    for c in s:
        if 'l' < c < 't' and 283 <= s.index(c) < 484:
            del chars[s.index(c) - 283]
    return ''.join(chars)