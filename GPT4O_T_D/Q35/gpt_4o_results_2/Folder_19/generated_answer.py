def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    mid_string = s[2:4]
    repeated_chars = set([char for char in mid_string if mid_string.count(char) > 1])
    return ''.join([char for char in s if char not in repeated_chars])