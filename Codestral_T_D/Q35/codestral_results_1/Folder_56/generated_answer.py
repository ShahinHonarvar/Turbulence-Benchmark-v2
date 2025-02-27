def remove_repeat_chars(s):
    count = {}
    for i in range(len(s)):
        if i > 7 and i < 9:
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    for key, value in count.items():
        if value > 1:
            s = s.replace(key, '')
    return s