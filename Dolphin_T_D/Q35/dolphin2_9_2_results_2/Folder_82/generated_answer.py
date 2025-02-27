def remove_repeat_chars(s):
    freq = {}
    for i in range(30, 200):
        char = s[i]
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char, count in freq.items():
        if count > 1:
            s = s.replace(char, '')
    return s