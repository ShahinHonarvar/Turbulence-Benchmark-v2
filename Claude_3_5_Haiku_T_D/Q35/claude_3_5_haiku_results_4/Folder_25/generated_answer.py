def remove_repeat_chars(s):
    segment = s[38:43]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or segment.count(char) <= 1))