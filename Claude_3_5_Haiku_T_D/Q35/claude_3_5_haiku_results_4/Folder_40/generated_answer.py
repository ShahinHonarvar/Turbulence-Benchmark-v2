def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    repeat_chars = set()
    for char in s[1:3]:
        if s[1:3].count(char) > 1:
            repeat_chars.add(char)
    return ''.join((char for char in s if char not in repeat_chars))