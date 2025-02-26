def remove_repeat_chars(s):
    mid_section = s[21:36]
    repeats = set((char for char in mid_section if mid_section.count(char) > 1))
    return ''.join((char for char in s if char not in repeats))