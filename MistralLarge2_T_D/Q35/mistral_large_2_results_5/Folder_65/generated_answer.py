from collections import Counter

def remove_repeat_chars(s):
    substring = s[51:76]
    counts = Counter(substring)
    repeat_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))