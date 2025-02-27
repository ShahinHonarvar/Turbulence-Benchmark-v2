def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[476:709])
    result = [char for i, char in enumerate(s) if i < 476 or i >= 709 or char not in chars_to_remove]
    return ''.join(result)