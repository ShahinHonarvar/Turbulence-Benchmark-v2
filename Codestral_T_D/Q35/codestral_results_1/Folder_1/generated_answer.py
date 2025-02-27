def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(17, 88):
        if s[i] in s[17:88] and s.count(s[i]) > 1:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))