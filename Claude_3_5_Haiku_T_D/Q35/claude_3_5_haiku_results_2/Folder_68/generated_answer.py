def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    chars_seen = {}
    repeat_chars = set()
    for i in range(1, 9):
        if s[i] in chars_seen:
            repeat_chars.add(s[i])
        else:
            chars_seen[s[i]] = 1
    return ''.join((char for char in s if char not in repeat_chars))