def remove_repeat_chars(s):
    freq = {}
    for i in range(20, 200):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for ch, count in freq.items():
        if count > 1:
            s = ''.join([c for c in s if c != ch])
    return s