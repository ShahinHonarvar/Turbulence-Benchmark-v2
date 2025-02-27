def remove_repeat_chars(s):
    freq = {}
    for i in range(30, 200):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for c in freq:
        if freq[c] > 1:
            s = s.replace(c, '')
    return s