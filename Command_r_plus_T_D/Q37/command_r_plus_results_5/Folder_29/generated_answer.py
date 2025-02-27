def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 12 <= s.index(c) <= 88 and '&' <= c <= 'v']
    return s.translate(str.maketrans('', '', ''.join(filtered_chars)))