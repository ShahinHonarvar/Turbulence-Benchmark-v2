def filter_chars(s: str) -> str:
    filter_range = range(19, 33)
    filter_chars_set = set('fghijklmno')
    return ''.join((c for i, c in enumerate(s) if i not in filter_range or c not in filter_chars_set))