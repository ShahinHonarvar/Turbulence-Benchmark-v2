def remove_repeat_chars(s):
    if len(s) <= 450:
        return s
    segment = s[451:905]
    repeats = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) < 451 or s.index(char) >= 905))
    return result