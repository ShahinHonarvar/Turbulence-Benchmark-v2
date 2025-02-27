def remove_repeat_chars(s):
    sub_str = s[70:98]
    repeated_chars = set((char for char in sub_str if sub_str.count(char) > 1))
    return ''.join((char for char in s if char not in repeated_chars))