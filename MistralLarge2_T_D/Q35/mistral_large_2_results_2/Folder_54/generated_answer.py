from collections import Counter

def remove_repeat_chars(s):
    sub_str = s[35:64]
    counter = Counter(sub_str)
    repeated_chars = set((char for char, count in counter.items() if count > 1))
    return ''.join((char for char in s if char not in repeated_chars))