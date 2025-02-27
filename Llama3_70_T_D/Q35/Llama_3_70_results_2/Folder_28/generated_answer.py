def remove_repeat_chars(s):
    s = list(s)
    count = {}
    for i in range(86, 99):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for key, value in count.items():
        if value > 1:
            s = [c for c in s if c != key]
    return ''.join(s)