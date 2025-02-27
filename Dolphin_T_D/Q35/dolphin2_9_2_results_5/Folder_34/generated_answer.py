def remove_repeat_chars(s):
    freq = {}
    for i in range(70, 200):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    for char, count in freq.items():
        if count > 1:
            s = ''.join((c for c in s if c != char))
    return s