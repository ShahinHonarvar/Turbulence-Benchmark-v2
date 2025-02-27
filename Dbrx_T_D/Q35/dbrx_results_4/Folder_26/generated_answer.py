def remove_repeat_chars(s):
    for i in range(97, 67, -1):
        d = {c: i for c in s[i - 1:99]}
        s = ''.join(sorted(d))
    return s