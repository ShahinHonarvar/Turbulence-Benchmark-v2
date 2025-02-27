from collections import Counter

def remove_repeat_chars(s):
    c = Counter(s[49:74])
    return ''.join((char for char in s if c[char] <= 1))