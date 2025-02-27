def remove_repeat_chars(s):
    repeating_chars = [char for char in set(s[1:5]) if s[1:5].count(char) > 1]
    return ''.join([char for char in s if char not in repeating_chars])