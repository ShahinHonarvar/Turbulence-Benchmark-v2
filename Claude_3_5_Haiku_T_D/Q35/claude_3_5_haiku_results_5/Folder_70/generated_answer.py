def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    segment = s[44:70]
    repeated_chars = set((char for char in segment if segment.count(char) > 1))
    result = s[:44] + ''.join((char for char in segment if char not in repeated_chars)) + s[70:]
    return result