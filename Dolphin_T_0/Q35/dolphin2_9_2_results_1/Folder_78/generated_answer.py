def remove_repeat_chars(s):
    chars_between_62_and_96 = s[62:96]
    unique_chars = set(chars_between_62_and_96)
    repeat_chars = [char for char in unique_chars if chars_between_62_and_96.count(char) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s