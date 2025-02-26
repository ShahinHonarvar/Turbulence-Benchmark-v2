def remove_repeat_chars(s):
    slice_to_check = s[11:28]
    chars_to_remove = set([char for char in slice_to_check if slice_to_check.count(char) > 1])
    return ''.join([char for char in s if char not in chars_to_remove])