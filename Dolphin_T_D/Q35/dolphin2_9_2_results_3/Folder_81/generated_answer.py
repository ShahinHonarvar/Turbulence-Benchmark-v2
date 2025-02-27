def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(20, 200):
        if s.count(s[i]) > 1:
            repeat_chars.add(s[i])
    return ''.join((char for char in s if char not in repeat_chars))