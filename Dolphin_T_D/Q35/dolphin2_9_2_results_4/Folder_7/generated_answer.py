def remove_repeat_chars(s):
    s = list(s)
    freq = {}
    for i in range(375, 926):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for char, count in freq.items():
        if count > 1:
            s = [c for c in s if c != char]
    return ''.join(s)