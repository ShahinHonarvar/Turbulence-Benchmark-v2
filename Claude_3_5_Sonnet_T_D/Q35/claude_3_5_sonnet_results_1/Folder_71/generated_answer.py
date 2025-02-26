def remove_repeat_chars(s):
    section = s[21:35]
    repeats = set((char for char in section if section.count(char) > 1))
    return ''.join((char for char in s if char not in repeats))