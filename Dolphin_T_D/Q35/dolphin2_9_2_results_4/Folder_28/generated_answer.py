def remove_repeat_chars(s):
    repeated_chars = [char for char in s[86:99] if s.count(char) > 1]
    s = ''.join((char for char in s if char not in repeated_chars))
    return s