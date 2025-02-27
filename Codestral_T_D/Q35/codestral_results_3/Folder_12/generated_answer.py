def remove_repeat_chars(s):
    chars = set(s[16:87])
    result = ''.join((char for char in s if s.count(char) == 1 or char not in chars))
    return result