def remove_repeat_chars(s):
    freq = {}
    for i in range(48, 76):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    for char in freq:
        if freq[char] > 1:
            s = s.replace(char, '')
    return s