def remove_repeat_chars(s):
    count = {}
    for i in s[:4]:
        if i != s[3]:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    for keys in list(count.keys()):
        if count[keys] > 1:
            s = s.replace(keys, '')
    return s