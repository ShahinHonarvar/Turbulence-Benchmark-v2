def remove_repeat_chars(s):
    freq = {}
    for i in range(38, 81):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    for key in list(freq):
        if freq[key] > 1:
            s = s.replace(key, '')
    return s