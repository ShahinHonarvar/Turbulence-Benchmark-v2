def remove_repeat_chars(s):
    if len(s) <= 7:
        return s
    substring = s[7:9]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 6 or s.index(char) >= 9))