from collections import Counter

def remove_repeat_chars(s):
    if len(s) <= 26:
        return s
    substring = s[26:80]
    char_count = Counter(substring)
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 26 or s.index(char) > 80))