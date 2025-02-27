def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if not (20 <= i <= 79 and ord(c) <= ord('T') and (ord(c) >= ord('!')))]
    return ''.join(filtered_chars)