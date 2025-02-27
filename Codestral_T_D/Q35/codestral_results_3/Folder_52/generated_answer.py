def remove_repeat_chars(s):
    sub_s = s[38:81]
    repeat_chars = [c for c in sub_s if sub_s.count(c) > 1]
    for char in set(repeat_chars):
        s = s.replace(char, '')
    return s