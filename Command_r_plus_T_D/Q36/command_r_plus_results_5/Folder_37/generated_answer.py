def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('/'), ord('6'))]
    filtered_string = ''.join([c for c in s if c not in chars_to_remove or s.index(c) not in range(44, 59)])
    return filtered_string