def remove_repeat_chars(s):
    freq = {}
    for i in range(476, 710):
        if i < len(s):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
    for key in freq:
        if freq[key] > 1:
            s = s.replace(key, '')
    return s