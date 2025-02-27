def remove_repeat_chars(s):
    sub_s = s[13:91]
    repeat_chars = set((char for char in sub_s if sub_s.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))