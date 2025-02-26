def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    substring = s[3:7]
    repeated_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 3 or s.index(char) >= 7))
    return result