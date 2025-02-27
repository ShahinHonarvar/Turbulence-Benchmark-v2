def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not ('f' < c < 'o' and 23 < s.index(c) < 83)]
    return ''.join(filtered_chars)