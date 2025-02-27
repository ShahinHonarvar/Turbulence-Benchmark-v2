def remove_repeat_chars(s):
    char_set = set()
    repeat_chars = set()
    for i in range(30, 200):
        if s[i] in char_set:
            repeat_chars.add(s[i])
        else:
            char_set.add(s[i])
    new_s = ''.join([c for c in s if c not in repeat_chars])
    return new_s