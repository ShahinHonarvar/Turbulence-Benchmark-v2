def remove_repeat_chars(s):
    freq = {}
    for i in range(2, 5):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for ch, count in freq.items():
        if count > 1:
            s = s.replace(ch, '')
    return s