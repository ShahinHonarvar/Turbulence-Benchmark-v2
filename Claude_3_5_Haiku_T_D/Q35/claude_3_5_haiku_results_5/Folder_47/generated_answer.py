def remove_repeat_chars(s):
    if len(s) <= 53:
        return s
    substr = s[30:53]
    repeated_chars = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in repeated_chars or s.index(char) < 30 or s.index(char) >= 53))
    return result