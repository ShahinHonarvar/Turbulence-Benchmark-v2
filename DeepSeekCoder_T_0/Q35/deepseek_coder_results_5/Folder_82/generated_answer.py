def remove_repeat_chars(s):
    if len(s) < 201:
        s = s[:30] + ''.join([char for i, char in enumerate(s[30:]) if s[30:].count(char) == 1])
    return s