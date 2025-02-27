def remove_repeat_chars(s):
    chars = [s[i] for i in range(86, 90) if s.count(s[i]) > 1]
    for c in chars:
        s = ''.join([x for x in s if x != c])
    return s