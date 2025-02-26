def remove_repeat_chars(s):
    if len(s) <= 462:
        return s
    check_slice = s[463:995]
    chars_to_remove = set()
    for char in check_slice:
        if check_slice.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))