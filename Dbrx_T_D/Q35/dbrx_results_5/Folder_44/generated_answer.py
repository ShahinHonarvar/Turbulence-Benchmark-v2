def remove_repeat_chars(s: str) -> str:
    start, end = (36, 52)
    chars_to_remove = set(s[start:end])
    for c in chars_to_remove:
        s = s.replace(c, '', start - end)
    return s