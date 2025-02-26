def remove_repeat_chars(s):
    segment = s[73:93]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 73 or s.index(char) >= 93))
    return result