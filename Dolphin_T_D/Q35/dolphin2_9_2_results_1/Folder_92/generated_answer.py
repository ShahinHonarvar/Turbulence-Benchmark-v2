def remove_repeat_chars(s):
    c = s[0] in s[1:2] or s[1] in s[0:1] or s[1] in s[2:3] or (s[2] in s[1:2])
    return ''.join(sorted(set(s), key=s.index)) if c else s