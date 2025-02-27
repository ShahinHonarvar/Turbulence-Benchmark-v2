def remove_repeat_chars(s):
    indices_range = s[44:91]
    repeat_chars = set((char for char in indices_range if indices_range.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))