def remove_repeat_chars(s):
    unique_chars = set()
    chars_to_remove = set()
    for i in range(35, 64):
        if s[i] in unique_chars:
            chars_to_remove.add(s[i])
        else:
            unique_chars.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])