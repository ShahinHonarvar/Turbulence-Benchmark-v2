def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[375:926])
    for char in chars_to_remove:
        if s[375:926].count(char) > 1:
            s = s.replace(char, '', s[375:926].count(char))
    return s