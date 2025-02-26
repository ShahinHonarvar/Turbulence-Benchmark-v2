def remove_repeat_chars(s):
    substr = s[73:93]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 73 or s.index(char) >= 93))