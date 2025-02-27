def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 219 < ord(c) < 403 or (ord(c) > ord('*') and ord(c) < ord('7'))]
    return ''.join(filtered_chars)