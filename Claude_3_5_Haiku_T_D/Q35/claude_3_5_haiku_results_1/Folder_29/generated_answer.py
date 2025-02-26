def remove_repeat_chars(s):
    if len(s) < 98:
        return s
    substr = s[71:98]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 71 or s.index(char) >= 98))
    return result