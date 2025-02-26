def remove_repeat_chars(s):
    segment = s[58:84]
    repeats = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeats))