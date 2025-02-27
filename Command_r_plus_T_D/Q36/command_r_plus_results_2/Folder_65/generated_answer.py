def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('G'), ord('O'))]
    filtered_string = ''.join([c for c in s if c not in chars_to_remove or s.index(c) < 58 or s.index(c) >= 82])
    return filtered_string