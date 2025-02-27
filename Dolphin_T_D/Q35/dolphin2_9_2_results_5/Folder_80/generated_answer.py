def remove_repeat_chars(s):
    freq = {}
    for i in range(57, 85):
        if not s[i] in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    for key in list(freq.keys()):
        if freq[key] > 1:
            s = s.replace(key, '')
    return s