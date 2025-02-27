def filter_chars(s: str) -> str:
    filter_chars_list = [c for c in s if not (ord(c) > 37 and ord(c) < 97)]
    return ''.join(filter_chars_list)