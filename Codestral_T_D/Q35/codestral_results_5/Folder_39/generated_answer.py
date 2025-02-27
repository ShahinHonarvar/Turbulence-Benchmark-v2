def remove_repeat_chars(s):
    cnt = {}
    for c in s[44:91]:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    return ''.join([c for c in s if cnt.get(c, 0) <= 1])