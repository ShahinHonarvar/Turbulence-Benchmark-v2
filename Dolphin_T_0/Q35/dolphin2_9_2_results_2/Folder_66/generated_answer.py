def remove_repeat_chars(s):
    freq = {}
    for i in range(11, 76):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    res = ''
    for i in range(len(s)):
        if i < 11 or i > 76 or freq[s[i]] == 1:
            res += s[i]
    return res