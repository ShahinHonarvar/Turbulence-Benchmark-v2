def remove_repeat_chars(s):
    if len(s) <= 104:
        return s
    segment = s[104:802]
    repeats = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 104 or s.index(char) >= 802))
    return result