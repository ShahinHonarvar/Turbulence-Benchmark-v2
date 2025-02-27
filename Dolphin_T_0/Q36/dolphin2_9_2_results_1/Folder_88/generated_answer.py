def filter_chars(s):
    chars = [s[i] for i in range(78, 81)]
    for c in chars:
        if 'S' < c < '[':
            s = ''.join([x for x in s if x != c])
    return s