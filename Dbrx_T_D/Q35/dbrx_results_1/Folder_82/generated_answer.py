def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[30:200])
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)