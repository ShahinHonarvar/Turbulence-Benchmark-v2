def remove_repeat_chars(s):
    count = {}
    for ch in s[32:44]:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in count:
        if count[ch] > 1:
            s = s.replace(ch, '')
    return s