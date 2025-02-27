def remove_repeat_chars(s):
    count = {}
    for i in range(55, 84):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    for ch in count:
        if count[ch] > 1:
            s = s.replace(ch, '')
    return s