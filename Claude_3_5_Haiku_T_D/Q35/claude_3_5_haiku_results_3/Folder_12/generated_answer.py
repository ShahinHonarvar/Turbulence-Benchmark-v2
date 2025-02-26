def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    segment = s[17:87]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 17 or s.index(char) >= 87))
    return result