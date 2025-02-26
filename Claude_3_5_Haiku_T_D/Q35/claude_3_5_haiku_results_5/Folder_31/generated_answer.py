def remove_repeat_chars(s):
    if len(s) <= 34:
        return s
    section = s[34:78]
    repeats = set((char for char in section if section.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) >= 78 or s.index(char) <= 33))
    return result