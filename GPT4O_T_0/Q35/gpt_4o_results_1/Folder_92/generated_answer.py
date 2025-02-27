def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    middle_section = s[1:2]
    repeated_chars = {char for char in middle_section if middle_section.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))