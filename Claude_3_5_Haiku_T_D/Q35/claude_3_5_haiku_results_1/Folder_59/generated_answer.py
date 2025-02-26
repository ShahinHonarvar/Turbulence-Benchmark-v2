def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    chars_in_range = s[1:10]
    chars_to_remove = set()
    for char in chars_in_range:
        if chars_in_range.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.add(char)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result