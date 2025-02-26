def remove_repeat_chars(s):
    section = s[57:88]
    chars_to_remove = set((char for char in section if section.count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))