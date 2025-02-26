def remove_repeat_chars(s):
    target_slice = s[51:76]
    chars_to_remove = set()
    for char in target_slice:
        if target_slice.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))