def remove_repeat_chars(s):
    to_remove = {char for i, char in enumerate(s) if 39 < i < 43 and s.count(char) > 1}
    return ''.join([char for char in s if char not in to_remove])