def remove_repeat_chars(s):
    chars_to_remove = set((char for char in set(s[56:88]) if s[56:88].count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))