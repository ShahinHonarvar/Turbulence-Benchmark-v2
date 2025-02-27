def filter_chars(s):
    start, end = (31, 50)
    chars_to_filter = {chr(i) for i in range(ord('/')) if ord('/') < i < ord('J')}
    return ''.join((c for i, c in enumerate(s) if i < start or i >= end or c not in chars_to_filter))