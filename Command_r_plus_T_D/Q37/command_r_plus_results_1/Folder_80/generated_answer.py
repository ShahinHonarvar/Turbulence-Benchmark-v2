def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('a'), ord('i') + 1)]
    filtered_string = ''.join([c for c in s if c not in chars_to_remove or 36 <= s.index(c) <= 79])
    return filtered_string