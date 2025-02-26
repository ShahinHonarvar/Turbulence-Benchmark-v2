def remove_repeat_chars(s):
    if len(s) <= 28:
        return s
    segment = s[28:96]
    chars_to_remove = set()
    for char in segment:
        if segment.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.add(char)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result