def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[36:54] if s[36:54].count(char) > 1])
    return ''.join([char for char in s if char not in repeat_chars])