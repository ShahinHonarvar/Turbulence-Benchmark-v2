def remove_repeat_chars(s):
    repeated_chars = set([char for char in s[2:4] if s[2:4].count(char) > 1])
    return ''.join([char for char in s if char not in repeated_chars])