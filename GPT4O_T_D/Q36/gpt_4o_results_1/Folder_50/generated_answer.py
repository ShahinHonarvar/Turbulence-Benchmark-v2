def filter_chars(s):
    to_remove = set()
    for ch in s[62:88]:
        if '%' < ch < 'q':
            to_remove.add(ch)
    return ''.join((ch for ch in s if ch not in to_remove))