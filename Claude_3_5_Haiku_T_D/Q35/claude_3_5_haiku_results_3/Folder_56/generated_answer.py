def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    segment = s[8:10]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars))
    return result