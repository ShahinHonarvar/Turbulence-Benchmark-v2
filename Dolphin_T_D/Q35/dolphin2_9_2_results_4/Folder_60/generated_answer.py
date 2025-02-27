def remove_repeat_chars(s):
    freq = {}
    for i in range(38, 52):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    for char, count in freq.items():
        if count > 1:
            s = s.replace(char, '')
    return s