def remove_repeat_chars(s):
    chars_to_remove = [s[i] for i in range(1, len(s) - 1) if s.count(s[i]) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s