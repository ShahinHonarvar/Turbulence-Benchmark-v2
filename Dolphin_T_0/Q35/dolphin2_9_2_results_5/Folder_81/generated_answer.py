def remove_repeat_chars(s):
    freq = {}
    for i in range(20, 200):
        freq[s[i]] = freq.get(s[i], 0) + 1
    for char in freq:
        if freq[char] > 1:
            s = s.replace(char, '')
    return s