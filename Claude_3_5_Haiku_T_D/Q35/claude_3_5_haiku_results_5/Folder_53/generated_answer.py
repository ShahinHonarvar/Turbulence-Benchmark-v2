def remove_repeat_chars(s):
    if len(s) <= 203:
        return s
    segment = s[201:203]
    repeats = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeats))