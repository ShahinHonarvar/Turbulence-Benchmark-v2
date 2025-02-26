def remove_repeat_chars(s):
    if len(s) <= 49:
        return s
    substr = s[46:48]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 45 or s.index(char) >= 48))
    return result