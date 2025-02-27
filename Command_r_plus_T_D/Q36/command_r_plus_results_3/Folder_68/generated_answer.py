def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('8') + 1, ord('m'))]
    filtered_string = ''.join((c for c in s if c not in chars_to_remove))
    return filtered_string