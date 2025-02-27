def remove_repeat_chars(s):
    chars_to_remove = set(s[68:99])
    for char in chars_to_remove:
        if s[68:99].count(char) > 1:
            s = s.replace(char, '', s[68:99].index(char))
    return s