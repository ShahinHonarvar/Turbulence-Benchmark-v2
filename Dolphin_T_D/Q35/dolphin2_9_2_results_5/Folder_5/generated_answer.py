def remove_repeat_chars(s):
    freq = {}
    for i in range(2, 8):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    for char in freq:
        if freq[char] > 1 and char in s:
            s = s.replace(char, '')
    return s