def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    substring = s[8:10]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 8 or s.index(char) >= 10))
    return result