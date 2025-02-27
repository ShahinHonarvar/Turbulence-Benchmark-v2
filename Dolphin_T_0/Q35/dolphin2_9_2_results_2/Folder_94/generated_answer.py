def remove_repeat_chars(s):
    freq = {}
    for char in s[42:87]:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    for char, count in freq.items():
        if count > 1:
            s = s.replace(char, '')
    return s