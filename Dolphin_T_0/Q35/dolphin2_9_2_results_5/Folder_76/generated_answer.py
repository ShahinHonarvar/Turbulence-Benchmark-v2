def remove_repeat_chars(s):
    freq = {}
    for i in range(330, 543):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    repeat_chars = [k for k, v in freq.items() if v > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s