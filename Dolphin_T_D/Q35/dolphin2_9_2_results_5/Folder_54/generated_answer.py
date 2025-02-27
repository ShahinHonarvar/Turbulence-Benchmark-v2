def remove_repeat_chars(s):
    cnt = {}
    for i in range(35, 65):
        if s[i] in cnt:
            cnt[s[i]] += 1
        else:
            cnt[s[i]] = 1
    for key in cnt:
        if cnt[key] > 1:
            s = s.replace(key, '')
    return s