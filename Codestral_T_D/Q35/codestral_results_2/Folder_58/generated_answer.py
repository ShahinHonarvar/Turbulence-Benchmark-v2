def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(104, 802):
        if i < len(s) and s[i] in s[i + 1:802]:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))