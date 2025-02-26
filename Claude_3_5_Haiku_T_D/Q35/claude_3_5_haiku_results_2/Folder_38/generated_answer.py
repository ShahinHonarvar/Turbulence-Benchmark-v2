def remove_repeat_chars(s):
    if len(s) <= 37:
        return s
    segment = s[37:85]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 37 or s.index(char) >= 85))
    return result