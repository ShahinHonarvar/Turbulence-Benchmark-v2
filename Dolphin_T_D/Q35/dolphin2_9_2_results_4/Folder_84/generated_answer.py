from collections import Counter

def remove_repeat_chars(s):
    c = Counter(s[32:44])
    for char in c:
        if c[char] > 1:
            s = ''.join([x for x in s if x != char])
    return s