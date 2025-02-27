def remove_repeat_chars(s):
    chars = s[70:98]
    repeat_chars = [char for char in set(chars) if chars.count(char) > 1]
    return ''.join((char for char in s if char not in repeat_chars))