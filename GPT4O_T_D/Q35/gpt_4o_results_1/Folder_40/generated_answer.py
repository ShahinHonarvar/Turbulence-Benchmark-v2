def remove_repeat_chars(s):
    section = s[1:3]
    to_remove = {char for char in section if section.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))