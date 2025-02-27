def remove_repeat_chars(s):
    res = ''
    freq = {}
    for i in range(69, 97):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    for i in range(len(s)):
        if s[i] not in freq or freq[s[i]] == 1:
            res += s[i]
    return res