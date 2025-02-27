def remove_repeat_chars(s):
    chars_10_100 = s[10:100]
    unique_chars = set(chars_10_100)
    to_remove = [char for char in unique_chars if chars_10_100.count(char) > 1]
    for char in to_remove:
        s = s.replace(char, '')
    return s