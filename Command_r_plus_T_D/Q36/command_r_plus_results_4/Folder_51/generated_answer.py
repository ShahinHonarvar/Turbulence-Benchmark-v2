def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (59 <= ord(c) <= 80 and ord(c) > 53 and (ord(c) < 62))]
    return ''.join(filtered_chars)