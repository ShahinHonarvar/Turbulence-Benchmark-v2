def remove_repeat_chars(s):
    chars_to_remove = [char for char, count in set(s[409:502]).items() if count > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s