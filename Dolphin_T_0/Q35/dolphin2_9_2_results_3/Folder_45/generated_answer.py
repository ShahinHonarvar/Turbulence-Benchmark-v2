def remove_repeat_chars(s):
    freq = {}
    for i in range(40, 200):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for key, value in freq.items():
        if value > 1:
            s = ''.join([c for c in s if c != key])
    return s