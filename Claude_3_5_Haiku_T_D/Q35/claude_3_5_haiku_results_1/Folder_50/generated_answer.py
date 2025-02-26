def remove_repeat_chars(s):
    if len(s) <= 14:
        return s
    substring = s[14:76]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 14 or s.index(char) >= 76))
    return result