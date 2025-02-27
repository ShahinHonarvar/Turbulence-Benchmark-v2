from collections import Counter

def remove_repeat_chars(s):
    counts = Counter(s[476:709])
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))