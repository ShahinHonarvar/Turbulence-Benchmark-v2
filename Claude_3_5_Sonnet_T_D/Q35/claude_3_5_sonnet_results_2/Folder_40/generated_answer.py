def remove_repeat_chars(s):
    check_range = s[1:3]
    repeated_chars = set([char for char in check_range if check_range.count(char) > 1])
    return ''.join([char for char in s if char not in repeated_chars])