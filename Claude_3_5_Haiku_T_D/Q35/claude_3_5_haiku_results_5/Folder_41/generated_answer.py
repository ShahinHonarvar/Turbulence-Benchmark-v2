def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    segment = s[4:8]
    repeats = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 4 or s.index(char) >= 8))
    return result