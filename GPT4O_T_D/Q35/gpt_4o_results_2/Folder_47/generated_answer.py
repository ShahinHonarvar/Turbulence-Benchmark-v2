from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 30:
        return s
    substring = s[30:53]
    counts = Counter(substring)
    to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove or not 30 < s.index(char) < 53))
    return result