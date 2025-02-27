def filter_chars(s: str) -> str:
    filter_chars_set = set(s[57:69]) & set(')+-./0123456789:;<=>?@ABCDEF')
    return ''.join((c for c in s if c not in filter_chars_set))