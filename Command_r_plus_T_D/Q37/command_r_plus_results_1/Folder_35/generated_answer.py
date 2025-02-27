def filter_chars(s: str) -> str:
    filter_range = range(155, 404)
    filter_chars = set(list('()[]'))
    filtered_string = ''.join((c for i, c in enumerate(s) if i not in filter_range or c not in filter_chars))
    return filtered_string