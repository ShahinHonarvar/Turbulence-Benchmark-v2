def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    segment = s[7:9]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 7 or s.index(char) > 8))
    return result