def remove_repeat_chars(s):
    count = {}
    for i in range(10):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    res = ''
    for i in s:
        if count[i] == 1:
            res += i
    return res