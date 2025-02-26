def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    substr = s[1:3]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))