def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('D'), ord('Y') + 1)]
    filtered_string = ''.join((c for c in s if c not in chars_to_remove or 225 <= s.index(c) <= 381))
    return filtered_string