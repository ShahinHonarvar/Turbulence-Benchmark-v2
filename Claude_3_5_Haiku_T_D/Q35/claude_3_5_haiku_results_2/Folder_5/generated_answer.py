def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    segment = s[3:8]
    repeats = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeats or s.index(char) < 3 or s.index(char) >= 8))