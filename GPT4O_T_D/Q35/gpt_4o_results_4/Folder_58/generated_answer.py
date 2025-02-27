def remove_repeat_chars(s):
    if len(s) <= 802:
        return s
    target_segment = s[104:802]
    chars_to_remove = {char for char in target_segment if target_segment.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))