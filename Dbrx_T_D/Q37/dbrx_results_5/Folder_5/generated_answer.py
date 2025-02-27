def filter_chars(s: str) -> str:
    chars_to_filter = set(range(ord('5'), ord('<') + 1))[24:83]
    filtered_chars = [c for i, c in enumerate(s) if i < 24 or i >= 82 or ord(c) not in chars_to_filter]
    return ''.join(filtered_chars)