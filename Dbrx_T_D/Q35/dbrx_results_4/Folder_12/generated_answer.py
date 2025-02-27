def remove_repeat_chars(s):
    chars = s[16:87]
    for char in chars:
        if chars.count(char) > 1:
            s = s.replace(char, '', chars.index(char))
    return s