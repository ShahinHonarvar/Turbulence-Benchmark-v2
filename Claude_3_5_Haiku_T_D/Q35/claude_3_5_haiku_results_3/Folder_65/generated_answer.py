def remove_repeat_chars(s):
    if len(s) <= 77:
        return s
    substr = s[52:76]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 52 or s.index(char) > 76))
    return result