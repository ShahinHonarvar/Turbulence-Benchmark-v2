def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in set(s[22:24]):
        if s[22:24].count(char) > 1:
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])