def remove_repeat_chars(s):
    repeat_chars = [char for char in s[28:96] if s[28:96].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])