def remove_repeat_chars(s):
    freq = {}
    for i in range(81, 87):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for ch in freq:
        if freq[ch] > 1:
            s = s.replace(ch, '')
    return s