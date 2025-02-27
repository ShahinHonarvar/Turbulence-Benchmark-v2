def remove_repeat_chars(s):
    chars = s[330:543]
    repeat_chars = [char for char in chars if chars.count(char) > 1]
    for char in set(repeat_chars):
        s = s.replace(char, '')
    return s