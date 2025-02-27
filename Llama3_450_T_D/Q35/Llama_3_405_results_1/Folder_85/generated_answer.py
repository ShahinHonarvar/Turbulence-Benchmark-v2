def remove_repeat_chars(s):
    repeats = [char for char in set(s[1:8]) if s[1:8].count(char) > 1]
    return ''.join([char for char in s if char not in repeats])