def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    segment = s[1:9]
    repeats = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 1 or s.index(char) >= 9))
    return result