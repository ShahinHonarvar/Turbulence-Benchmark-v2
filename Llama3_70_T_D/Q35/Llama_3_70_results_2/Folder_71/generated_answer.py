def remove_repeat_chars(s):
    mid_str = s[20:35]
    for char in set(mid_str):
        if mid_str.count(char) > 1:
            s = s.replace(char, '')
    return s