def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    substring = s[1:8]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 1 or s.index(char) >= 8))
    return result