def remove_repeat_chars(s):
    if len(s) <= 69:
        return s
    sub_string = s[70:97]
    chars_to_remove = {char for char in sub_string if sub_string.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 69 or s.index(char) >= 97))