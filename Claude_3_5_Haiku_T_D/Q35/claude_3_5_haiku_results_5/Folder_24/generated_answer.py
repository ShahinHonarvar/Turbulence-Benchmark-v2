def remove_repeat_chars(s):
    if len(s) <= 13 or len(s) <= 91:
        return s
    substring = s[14:91]
    repeated_chars = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 14 or s.index(char) >= 91))
    return result