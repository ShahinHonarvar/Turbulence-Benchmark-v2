def remove_repeat_chars(s: str) -> str:
    chars_between_indices_0_and_7 = set(s[1:8])
    for char in chars_between_indices_0_and_7:
        if s[1:8].count(char) > 1:
            s = s.replace(char, '', 8)
    return s