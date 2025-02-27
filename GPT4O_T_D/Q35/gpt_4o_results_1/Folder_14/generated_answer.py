def remove_repeat_chars(s):
    middle_section = s[3:5]
    chars_to_remove = {char for char in middle_section if middle_section.count(char) > 1}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result