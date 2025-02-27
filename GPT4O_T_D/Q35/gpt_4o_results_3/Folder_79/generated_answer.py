def remove_repeat_chars(s):
    midpoint_section = s[2:7]
    chars_to_remove = {char for char in midpoint_section if midpoint_section.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))