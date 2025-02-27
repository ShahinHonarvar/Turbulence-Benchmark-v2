def remove_repeat_chars(s):
    freq = {}
    for i in range(46, 92):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    repeats = [k for k, v in freq.items() if v > 1]
    for c in repeats:
        s = s.replace(c, '')
    return s