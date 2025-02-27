def filter_chars(s: str) -> str:
    filter_range = range(73, 75)
    filter_chars = set('U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')
    return ''.join((c for i, c in enumerate(s) if c not in filter_chars or i not in filter_range))