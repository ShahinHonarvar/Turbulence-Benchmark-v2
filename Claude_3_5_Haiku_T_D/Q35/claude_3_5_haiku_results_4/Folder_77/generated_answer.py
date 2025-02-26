def remove_repeat_chars(s):
    segment = s[356:988]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 356 or s.index(char) >= 988))