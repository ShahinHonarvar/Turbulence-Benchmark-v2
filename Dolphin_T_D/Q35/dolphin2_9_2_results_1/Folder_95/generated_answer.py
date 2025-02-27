def remove_repeat_chars(s):
    to_remove = [char for char in s if s.count(char) > 1 and 32 <= ord(char) <= 99]
    new_s = ''.join([char for char in s if char not in to_remove])
    return new_s