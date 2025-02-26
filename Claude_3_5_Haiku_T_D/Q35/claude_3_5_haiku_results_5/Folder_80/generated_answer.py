def remove_repeat_chars(s):
    if len(s) <= 58:
        return s
    substring = s[58:84]
    repeated_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 58 or s.index(char) >= 84))
    return result