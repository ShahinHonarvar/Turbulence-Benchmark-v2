def remove_repeat_chars(s):
    to_remove = [ch for ch, count in zip(s[51:76], s.count(ch)[51:76]) if count]
    for ch in to_remove:
        s = s.replace(ch, '')
    return s