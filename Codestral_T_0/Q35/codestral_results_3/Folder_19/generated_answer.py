def remove_repeat_chars(s):
    chars_to_remove = set((char for char in s[1:4] if s.count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))