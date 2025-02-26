def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    segment = s[4:9]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 4 or s.index(char) >= 9))