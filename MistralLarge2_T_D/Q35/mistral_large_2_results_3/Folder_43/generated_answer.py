def remove_repeat_chars(s):
    count = {}
    for i in range(10, 28):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    s = list(s)
    for i in range(len(s)):
        if s[i] in count and count[s[i]] > 1:
            s[i] = ''
    return ''.join(s)