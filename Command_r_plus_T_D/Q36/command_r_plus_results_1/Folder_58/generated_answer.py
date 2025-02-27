def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('B') + 1, ord('z'))]
    filtered_string = ''.join([c for c in s if c not in chars_to_remove or s.index(c) in range(318, 338)])
    return filtered_string