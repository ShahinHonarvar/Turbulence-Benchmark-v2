def remove_repeat_chars(s: str) -> str:
    if type(s) != str or len(s) < 709 or len(s) < 476:
        raise ValueError('Input string must be at least 709 characters long')
    chars_to_remove = set()
    for i in range(476, 709):
        if s[i] in chars_to_remove:
            s = s[:i] + s[i + 1:]
        else:
            chars_to_remove.add(s[i])
    return s