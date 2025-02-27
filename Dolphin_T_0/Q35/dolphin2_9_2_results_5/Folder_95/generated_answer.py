def remove_repeat_chars(s):
    counter = {}
    for c in s[32:99]:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    for c in s:
        if c in counter and counter[c] > 1:
            s = s.replace(c, '')
    return s