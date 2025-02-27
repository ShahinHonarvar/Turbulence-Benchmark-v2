def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('<'), ord('w') + 1)) & set(range(57, 97))
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result