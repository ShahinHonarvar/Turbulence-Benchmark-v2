def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(72, 93):
        if s.count(s[i], 72, 93) > 1:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))