def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('i'), ord('k') + 1)]
    filtered_string = ''.join([c for c in s if c not in chars_to_remove or 20 <= s.index(c) <= 62])
    return filtered_string