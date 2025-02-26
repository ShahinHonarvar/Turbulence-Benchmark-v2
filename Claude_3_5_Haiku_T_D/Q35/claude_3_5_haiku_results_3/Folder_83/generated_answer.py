def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    substring = s[101:200]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    return ''.join((char for char in s if char not in repeat_chars))