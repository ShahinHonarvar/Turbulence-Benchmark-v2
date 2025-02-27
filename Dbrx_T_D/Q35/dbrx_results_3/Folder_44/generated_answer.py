def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[36:52])
    result = [char for i, char in enumerate(s) if char not in chars_to_remove or i < 36 or i >= 52]
    return ''.join(result)