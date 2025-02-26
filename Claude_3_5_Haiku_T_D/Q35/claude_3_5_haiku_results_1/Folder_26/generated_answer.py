def remove_repeat_chars(s):
    segment = s[69:99]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 69 or s.index(char) > 98))
    return result