def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (47 <= ord(c) < 69 and 'H' < c < 's')]
    return ''.join(filtered_chars)