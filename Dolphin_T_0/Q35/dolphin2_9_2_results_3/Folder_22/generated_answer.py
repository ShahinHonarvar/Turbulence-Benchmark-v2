def remove_repeat_chars(s):
    char_set = set(s[50:200])
    remove_chars = []
    for char in char_set:
        if s.count(char) > 1:
            remove_chars.append(char)
    s = ''.join([c for c in s if c not in remove_chars])
    return s