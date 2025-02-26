def remove_repeat_chars(s):
    if len(s) <= 40:
        return s
    substring = s[21:93]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 21 or s.index(char) >= 93))
    return result