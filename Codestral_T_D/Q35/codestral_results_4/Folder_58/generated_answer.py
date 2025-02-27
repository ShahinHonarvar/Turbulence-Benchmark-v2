def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(104, 802):
        if s[i] in s[104:802] and s.count(s[i], 104, 802) > 1:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))