def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 46 < s.index(c) < 68 or not (c > 'H' and c < 's')]
    return ''.join(filtered_chars)