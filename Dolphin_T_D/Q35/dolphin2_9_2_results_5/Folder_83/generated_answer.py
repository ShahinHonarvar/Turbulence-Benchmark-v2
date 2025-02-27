def remove_repeat_chars(s):
    freq = {}
    for i in range(100, 200):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for char, count in freq.items():
        if count > 1:
            s = ''.join([x for x in s if x != char])
    return s