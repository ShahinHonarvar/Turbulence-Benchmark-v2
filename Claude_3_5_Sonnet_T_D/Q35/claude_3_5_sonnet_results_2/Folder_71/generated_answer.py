def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(21, 35):
        if i < len(s) and s[i] in s[21:35] and (s.count(s[i], 21, 35) > 1):
            repeat_chars.add(s[i])
    return ''.join((char for char in s if char not in repeat_chars))