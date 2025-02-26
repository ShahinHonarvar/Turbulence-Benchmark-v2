def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    substr = s[1:11]
    repeats = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in repeats or s.index(char) >= 11))
    return result