def remove_repeat_chars(s):
    chars_to_remove = [char for char in s[68:99] if s.count(char) > 1]
    new_s = ''.join([char for char in s if char not in chars_to_remove])
    return new_s