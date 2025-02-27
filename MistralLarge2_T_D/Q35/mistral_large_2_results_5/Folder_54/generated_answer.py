from collections import Counter

def remove_repeat_chars(s):
    sub_str = s[35:64]
    repeat_chars = [char for char, count in Counter(sub_str).items() if count > 1]
    return ''.join([char for char in s if char not in repeat_chars])