def remove_repeat_chars(s):
    freq = {}
    for i in range(13, 70):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for char, count in freq.items():
        if count > 1:
            s = s.replace(char, '')
    return s