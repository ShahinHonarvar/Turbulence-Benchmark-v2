def remove_repeat_chars(s):
    chars_to_remove = set((char for char in s[38:81] if s[38:81].count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))