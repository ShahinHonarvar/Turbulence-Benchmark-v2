def remove_repeat_chars(s):
    if len(s) <= 23:
        return s
    section = s[23:24]
    to_remove = {char for char in section if section.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))