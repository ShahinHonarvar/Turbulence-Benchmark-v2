def remove_repeat_chars(s):
    freq = {}
    for i in range(38, 81, 1):
        ch = s[i]
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch, count in freq.items():
        if count > 1:
            s = s.replace(ch, '')
    return s