def remove_repeat_chars(s):
    repeat_chars = [char for char in set(s[18:60]) if s[18:60].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])