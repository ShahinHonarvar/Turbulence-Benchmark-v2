def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    segment = s[11:100]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 11 or s.index(char) >= 100))