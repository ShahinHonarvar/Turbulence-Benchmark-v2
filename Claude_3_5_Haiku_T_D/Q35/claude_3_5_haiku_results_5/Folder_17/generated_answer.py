def remove_repeat_chars(s):
    if len(s) <= 74:
        return s
    substr = s[74:84]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 74 or s.index(char) >= 84))
    return result