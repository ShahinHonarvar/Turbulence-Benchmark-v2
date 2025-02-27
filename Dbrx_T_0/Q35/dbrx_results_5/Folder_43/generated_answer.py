def remove_repeat_chars(s):
    chars_to_remove = set(s[10:28])
    for char in chars_to_remove:
        if s[10:28].count(char) > 1:
            s = s.replace(char, '', s[10:28].index(char))
    return s