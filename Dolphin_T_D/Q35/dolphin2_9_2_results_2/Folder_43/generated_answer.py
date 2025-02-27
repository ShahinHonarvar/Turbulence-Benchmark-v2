def remove_repeat_chars(s):
    freq = {}
    for i in s[10:28]:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in s[10:28]:
        if freq[i] > 1:
            s = s.replace(i, '')
    return s