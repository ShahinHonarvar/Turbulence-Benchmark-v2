def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    middle_chars = s[1:6]
    repeat_chars = {char for char in middle_chars if middle_chars.count(char) > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result