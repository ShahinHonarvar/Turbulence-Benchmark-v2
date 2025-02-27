def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('_'), ord('o') + 1) if ord('_') <= i <= ord('o') and 71 <= i <= 96]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s