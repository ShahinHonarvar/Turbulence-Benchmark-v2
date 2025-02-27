def remove_repeat_chars(s):
    target_part = s[4:8]
    repeat_chars = {char for char in target_part if target_part.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))