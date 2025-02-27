def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(81, 86):
        if s[i:i + 1] in s[i + 1:86]:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))