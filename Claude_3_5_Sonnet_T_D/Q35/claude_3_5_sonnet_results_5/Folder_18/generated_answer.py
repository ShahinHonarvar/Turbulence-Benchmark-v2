def remove_repeat_chars(s):
    target_range = s[56:90]
    chars_to_remove = set((char for char in target_range if target_range.count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))