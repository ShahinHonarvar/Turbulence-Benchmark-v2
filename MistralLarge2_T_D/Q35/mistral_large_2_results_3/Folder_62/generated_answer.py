def remove_repeat_chars(s):
    target_range = s[50:92]
    repeat_chars = {char for char in target_range if target_range.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))