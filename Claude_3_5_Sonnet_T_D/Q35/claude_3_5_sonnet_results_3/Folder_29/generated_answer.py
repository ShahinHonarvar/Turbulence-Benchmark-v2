def remove_repeat_chars(s):
    segment = s[71:98]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeated_chars))