def remove_repeat_chars(s):
    substring = s[45:91]
    repeats = set((char for char in substring if substring.count(char) > 1))
    return ''.join((char for char in s if char not in repeats or s.index(char) < 45 or s.index(char) >= 91))