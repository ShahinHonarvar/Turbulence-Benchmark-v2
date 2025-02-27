def filter_chars(s):
    to_remove = set()
    for ch in s[42:56]:
        if 'Z' < ch < 'c':
            to_remove.add(ch)
    return ''.join((ch for ch in s if ch not in to_remove))