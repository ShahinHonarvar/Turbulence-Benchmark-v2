def remove_repeat_chars(s):
    target_chars = set(s[82:86])
    repeat_chars = set((char for char in target_chars if s[82:86].count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))