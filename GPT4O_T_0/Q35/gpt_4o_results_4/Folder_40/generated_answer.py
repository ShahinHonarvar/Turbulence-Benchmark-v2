def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    middle_section = s[1:3]
    chars_to_remove = {char for char in middle_section if middle_section.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))