def remove_repeat_chars(s):
    if len(s) <= 57:
        return s
    segment = s[57:90]
    repeats = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 57 or s.index(char) >= 90))
    return result