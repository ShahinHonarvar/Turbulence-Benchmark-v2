def remove_repeat_chars(s):
    if len(s) <= 52:
        return s
    segment = s[39:52]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeated_chars))