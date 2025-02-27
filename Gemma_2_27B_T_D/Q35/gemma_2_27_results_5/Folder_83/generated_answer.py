from collections import Counter

def remove_repeat_chars(s):
    counts = Counter(s[100:200])
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s