def remove_repeat_chars(s: str) -> str:
    unique_chars = s[374:925]
    for char in unique_chars:
        if unique_chars.count(char) > 1:
            s = s.replace(char, '', unique_chars.count(char))
    return s