def filter_chars(s):
    start, end = (40, 86)
    chars_to_remove = set(s[start:end + 1])
    chars_to_remove = {c for c in chars_to_remove if ord('S') <= ord(c) <= ord('s')}
    return ''.join((c for i, c in enumerate(s) if i < start or i > end or c not in chars_to_remove))