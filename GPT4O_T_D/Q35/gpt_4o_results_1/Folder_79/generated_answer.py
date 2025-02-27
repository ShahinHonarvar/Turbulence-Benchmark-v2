def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    check_section = s[2:7]
    chars_to_remove = {char for char in check_section if check_section.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))