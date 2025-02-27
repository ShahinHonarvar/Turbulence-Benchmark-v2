def remove_repeat_chars(s):
    freq = {}
    for i in range(62, 97):
        freq[s[i]] = freq.get(s[i], 0) + 1
    altered_s = ''
    for i in range(len(s)):
        if i < 62 or i >= 97 or freq[s[i]] == 1:
            altered_s += s[i]
    return altered_s