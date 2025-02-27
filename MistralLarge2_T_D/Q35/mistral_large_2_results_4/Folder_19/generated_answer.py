from collections import Counter

def remove_repeat_chars(s):
    count = Counter(s[1:4])
    return ''.join((char for char in s if count[char] <= 1))