from collections import Counter

def remove_repeat_chars(s):
    c = Counter(s[16:87])
    for char, count in c.items():
        if count > 1:
            s = s.replace(char, '')
    return s