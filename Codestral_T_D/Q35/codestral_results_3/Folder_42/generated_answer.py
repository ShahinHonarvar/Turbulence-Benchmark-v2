def remove_repeat_chars(s):
    to_remove = set((char for char in s[18:60] if s[18:60].count(char) > 1))
    return ''.join((char for char in s if char not in to_remove))