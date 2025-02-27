def remove_repeat_chars(s):
    from_index = 1
    to_index = 7
    sub_str = s[from_index:to_index]
    for char in set(sub_str):
        if sub_str.count(char) > 1:
            s = s.replace(char, '')
    return s