def filter_chars(s: str) -> str:
    filter_range = [chr(i) for i in range(62, 74)]
    filter_set = set(filter_range)
    return ''.join((c for c in s if c not in filter_set))