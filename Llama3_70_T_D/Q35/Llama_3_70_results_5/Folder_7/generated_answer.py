def remove_repeat_chars(s):
    count = {}
    for i in range(375, 926):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    res = []
    for char in s:
        if count.get(char, 0) == 1:
            res.append(char)
    return ''.join(res)