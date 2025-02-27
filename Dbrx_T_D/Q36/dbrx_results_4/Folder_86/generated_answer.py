def filter_chars(s):
    start, end = (672, 709)
    chars_to_remove = set(sorted(s[start - 1:end])[::-1]) & set(range(ord('X') + 1, ord('}') + 1))
    return ''.join((c for i, c in enumerate(s) if i not in (start, end) and c not in chars_to_remove))