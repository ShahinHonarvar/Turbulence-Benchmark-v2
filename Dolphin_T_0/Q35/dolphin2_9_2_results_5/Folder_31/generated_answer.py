def remove_repeat_chars(s):
    count = {}
    for i in range(33, 78):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for key, value in count.items():
        if value > 1:
            s = ''.join((c for c in s if c != key))
    return s