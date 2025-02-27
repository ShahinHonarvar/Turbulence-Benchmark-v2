def remove_repeat_chars(s):
    to_remove = [char for char in s[44:78] if s.count(char) > 1]
    for char in to_remove:
        s = s.replace(char, '')
    return s