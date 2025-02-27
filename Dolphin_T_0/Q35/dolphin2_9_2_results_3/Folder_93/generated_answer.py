def remove_repeat_chars(s):
    count = {}
    for i in range(57, 85):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for key in count:
        if count[key] > 1:
            s = ''.join([x for x in s if x != key])
    return s