def remove_repeat_chars(s: str) -> str:
    chars_between_55_and_84 = set(s[54:84])
    repeated_chars = set()
    for char in chars_between_55_and_84:
        if s[54:84].count(char) > 1:
            repeated_chars.add(char)
    for char in repeated_chars:
        s = s.replace(char, '', s[54:84].count(char))
    return s