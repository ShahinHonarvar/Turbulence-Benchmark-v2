def remove_repeat_chars(s):
    if len(s) <= 40:
        return s
    segment = s[21:35]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 21 or s.index(char) >= 35))
    return result