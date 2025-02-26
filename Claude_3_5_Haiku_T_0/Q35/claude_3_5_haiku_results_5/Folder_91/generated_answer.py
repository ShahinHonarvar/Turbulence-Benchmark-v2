def remove_repeat_chars(s):
    if len(s) <= 7:
        return s
    segment = s[1:6]
    chars_to_remove = set()
    for char in segment:
        if segment.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))