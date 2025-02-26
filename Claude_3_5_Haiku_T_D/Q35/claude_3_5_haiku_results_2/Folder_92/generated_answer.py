def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    first_segment = s[1:3]
    repeated_chars = set((char for char in first_segment if first_segment.count(char) > 1))
    return ''.join((char for char in s if char not in repeated_chars))