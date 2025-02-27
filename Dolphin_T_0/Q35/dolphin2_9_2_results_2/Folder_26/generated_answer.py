def remove_repeat_chars(s):
    count = {}
    for c in s[68:99]:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    for key in count:
        if count[key] > 1:
            s = s.replace(key, '')
    return s