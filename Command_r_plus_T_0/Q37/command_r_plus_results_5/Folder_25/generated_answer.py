def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not (31 <= ord(c) <= 38 and ord(c) >= ord(';') and (ord(c) <= ord('g')))))
    return filtered_string