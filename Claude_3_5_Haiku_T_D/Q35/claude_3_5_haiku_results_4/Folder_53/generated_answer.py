def remove_repeat_chars(s):
    if len(s) <= 203:
        return s
    segment = s[201:203]
    chars_to_remove = set()
    for char in segment:
        if segment.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))