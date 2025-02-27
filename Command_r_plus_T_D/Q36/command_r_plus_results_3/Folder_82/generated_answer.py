def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 69 < s.index(c) < 97 or not 'V' < c < 'j']
    return ''.join(filtered_chars)