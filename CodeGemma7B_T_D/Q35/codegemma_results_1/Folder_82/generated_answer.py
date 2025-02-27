from collections import Counter

def remove_repeat_chars(s):
    counts = Counter(s[30:200])
    return ''.join([c for c in s if counts[c] == 1])