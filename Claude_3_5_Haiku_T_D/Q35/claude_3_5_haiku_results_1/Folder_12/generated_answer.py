def remove_repeat_chars(s):
    if len(s) <= 16:
        return s
    substring = s[17:87]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 17 or s.index(char) >= 87))
    return result