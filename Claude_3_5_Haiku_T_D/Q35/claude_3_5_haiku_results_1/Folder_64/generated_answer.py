def remove_repeat_chars(s):
    if len(s) <= 6:
        return s
    segment = s[1:5]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) >= 6))