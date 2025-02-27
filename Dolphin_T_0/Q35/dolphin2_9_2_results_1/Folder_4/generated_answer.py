def remove_repeat_chars(s):
    chars_between = s[50:75]
    unique_chars = set(chars_between)
    for char in unique_chars:
        if chars_between.count(char) > 1:
            s = s.replace(char, '')
    return s