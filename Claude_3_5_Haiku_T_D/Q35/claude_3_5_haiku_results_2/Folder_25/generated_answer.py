def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    substring = s[38:43]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 37 or s.index(char) >= 43))
    return result