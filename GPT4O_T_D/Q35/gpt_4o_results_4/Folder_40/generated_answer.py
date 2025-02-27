def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    section = s[1:3]
    chars_to_remove = {char for char in section if section.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))