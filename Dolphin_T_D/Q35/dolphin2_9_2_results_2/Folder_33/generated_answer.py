def remove_repeat_chars(s):
    new_str = ''
    for c in s:
        if c not in new_str:
            new_str += c
    return new_str