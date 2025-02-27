from collections import Counter

def remove_repeat_chars(s):
    s = list(s)
    c = Counter(s[17:88])
    for k, v in c.items():
        if v > 1:
            s = [i for i in s if i != k]
    return ''.join(s)