def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    substr = s[19:60]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 18 or s.index(char) >= 60))
    return result