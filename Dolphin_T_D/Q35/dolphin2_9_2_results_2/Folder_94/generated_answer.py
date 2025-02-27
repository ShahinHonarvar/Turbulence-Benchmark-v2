def remove_repeat_chars(s):
    chars_remove = set()
    for char in s[42:87]:
        if s.count(char) > 1:
            chars_remove.add(char)
    s = ''.join([char for char in s if char not in chars_remove])
    return s