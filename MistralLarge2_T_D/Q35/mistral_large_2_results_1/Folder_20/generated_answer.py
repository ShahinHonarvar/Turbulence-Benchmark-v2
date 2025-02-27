from collections import Counter

def remove_repeat_chars(s):
    sub_str = s[27:96]
    counts = Counter(sub_str)
    repeated_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))