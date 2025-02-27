def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    section = s[57:88]
    removal_set = {char for char in section if section.count(char) > 1}
    return ''.join((char for char in s if char not in removal_set or s.index(char) >= 88 or s.index(char) <= 56))