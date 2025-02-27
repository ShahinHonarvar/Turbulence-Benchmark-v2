def remove_repeat_chars(s):
    to_remove = set((char for char in s[1:7] if s[1:7].count(char) > 1))
    return ''.join((char for char in s if char not in to_remove))