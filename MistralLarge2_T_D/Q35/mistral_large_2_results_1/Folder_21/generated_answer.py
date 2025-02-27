from collections import Counter

def remove_repeat_chars(s):
    substring = s[462:995]
    repeated_chars = [char for char, count in Counter(substring).items() if count > 1]
    for char in repeated_chars:
        s = s.replace(char, '')
    return s