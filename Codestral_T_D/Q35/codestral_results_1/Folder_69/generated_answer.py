def remove_repeat_chars(s):
    sub_str = s[39:43]
    chars_to_remove = [char for char in sub_str if sub_str.count(char) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s