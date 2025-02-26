def remove_repeat_chars(s):
    if len(s) <= 39:
        return s
    segment = s[39:81]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 39 or s.index(char) >= 81))
    return result