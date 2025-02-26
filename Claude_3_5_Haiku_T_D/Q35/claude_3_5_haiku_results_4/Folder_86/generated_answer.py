def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    substring = s[20:32]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 19 or s.index(char) >= 32))