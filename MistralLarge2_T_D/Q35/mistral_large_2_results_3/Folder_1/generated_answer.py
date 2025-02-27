def remove_repeat_chars(s):
    count = {}
    for i in range(17, 88):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''.join([s[i] for i in range(len(s)) if count.get(s[i], 0) <= 1])
    return result