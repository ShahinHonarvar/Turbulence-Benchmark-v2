def filter_chars(s: str) -> str:
    chars_to_filter = set(s[39:87])
    filtered_chars = {c for c in chars_to_filter if '!' < c < '}'}
    for c in filtered_chars:
        s = s.replace(c, '', s.count(c))
    return s