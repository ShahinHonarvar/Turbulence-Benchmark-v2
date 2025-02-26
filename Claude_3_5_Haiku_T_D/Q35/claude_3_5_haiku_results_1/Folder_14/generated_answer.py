def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    segment = s[3:5]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 3 or s.index(char) >= 5))
    return result