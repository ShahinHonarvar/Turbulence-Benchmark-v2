from collections import Counter

def remove_repeat_chars(s):
    c = Counter(s[20:51])
    for char, _ in c.items():
        s = s.replace(char, '')
    return s