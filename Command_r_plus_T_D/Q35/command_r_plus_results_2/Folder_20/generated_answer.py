def remove_repeat_chars(s: str) -> str:
    filtered_chars = [c for c in s if s.count(c) == 1 and 27 <= ord(c) < 96]
    return ''.join(filtered_chars)