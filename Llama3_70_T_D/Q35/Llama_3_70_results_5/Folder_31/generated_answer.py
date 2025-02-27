def remove_repeat_chars(s):
    chars_to_remove = [char for char in set(s[33:78]) if s[33:78].count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])