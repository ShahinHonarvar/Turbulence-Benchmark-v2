def remove_repeat_chars(s):
    sub = s[42:87]
    repeated_chars = set((char for char in sub if sub.count(char) > 1))
    return ''.join((char for char in s if char not in repeated_chars))