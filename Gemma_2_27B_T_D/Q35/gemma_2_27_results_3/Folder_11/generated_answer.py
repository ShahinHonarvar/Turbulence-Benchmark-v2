from collections import Counter

def remove_repeat_chars(s):
    char_counts = Counter(s[48:76])
    for char, count in char_counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s