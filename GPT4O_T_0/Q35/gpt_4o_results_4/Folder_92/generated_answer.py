def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    middle_chars = s[1:2]
    repeat_chars = {char for char in middle_chars if middle_chars.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))