def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in set(s[29:53]):
        if s[29:53].count(char) > 1:
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])