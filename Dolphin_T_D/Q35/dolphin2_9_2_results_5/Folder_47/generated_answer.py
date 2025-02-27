def remove_repeat_chars(s):
    freq = {}
    for i in range(29, 53):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for i in range(29, 53):
        if freq[s[i]] > 1:
            s = s.replace(s[i], '')
    return s