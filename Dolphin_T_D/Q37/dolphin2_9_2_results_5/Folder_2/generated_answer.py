def filter_chars(s):
    to_delete = set()
    for i in range(477, 985):
        c = s[i]
        if c >= ',' and c <= 'V':
            to_delete.add(c)
    out = ''
    for c in s:
        if c not in to_delete:
            out += c
    return out