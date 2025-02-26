def remove_repeat_chars(s):
    segment = s[81:86]
    chars_to_remove = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))