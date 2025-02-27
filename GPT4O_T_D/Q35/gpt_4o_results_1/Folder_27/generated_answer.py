def remove_repeat_chars(s):
    if len(s) <= 89:
        return s
    chars_to_check = s[87:89]
    repeat_chars = {char for char in chars_to_check if chars_to_check.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))