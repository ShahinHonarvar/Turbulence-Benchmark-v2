def filter_chars(s: str) -> str:
    filtered_string = ''.join((ch for ch in s if not (27 <= ord(ch) <= 85 and 'c' <= ch <= 'i')))
    return filtered_string