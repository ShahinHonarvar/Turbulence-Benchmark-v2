from collections import Counter

def remove_repeat_chars(s):
    substring = s[125:825]
    repeated_chars = set((char for char, count in Counter(substring).items() if count > 1))
    return ''.join((char for char in s if char not in repeated_chars))