def remove_repeat_chars(s):
    if len(s) <= 40:
        return s
    target_slice = s[40:43]
    repeated_chars = set([char for char in target_slice if target_slice.count(char) > 1])
    return ''.join([char for char in s if char not in repeated_chars])