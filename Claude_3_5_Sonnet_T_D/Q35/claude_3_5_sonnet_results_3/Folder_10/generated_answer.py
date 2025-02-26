def remove_repeat_chars(s):
    section = s[37:54]
    repeat_chars = set((char for char in section if section.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))