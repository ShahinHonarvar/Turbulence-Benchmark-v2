def remove_repeat_chars(s):
    chars_to_remove = set((char for char in s[25:80] if s[25:80].count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))