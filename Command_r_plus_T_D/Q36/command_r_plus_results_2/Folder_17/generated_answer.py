def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if 18 <= i < 95 and 'K' < c < 'a' or 18 > i >= 95))
    return filtered_string