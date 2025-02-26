def remove_repeat_chars(s):
    if len(s) <= 104:
        return s
    segment = s[104:802]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 104 or s.index(char) >= 802))