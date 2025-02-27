def remove_repeat_chars(s):
    chars_to_remove = [char for char in s[125:825] if s[125:825].count(char) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s