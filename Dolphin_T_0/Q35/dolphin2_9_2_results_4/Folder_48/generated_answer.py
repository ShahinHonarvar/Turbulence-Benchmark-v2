def remove_repeat_chars(s):
    freq = {}
    for i in range(409, 502):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for char in freq:
        while freq[char] > 1:
            s = s.replace(char, '')
        freq[char] = 0
    return s