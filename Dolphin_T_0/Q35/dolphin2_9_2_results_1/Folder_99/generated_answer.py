def remove_repeat_chars(s):
    freq = {}
    for i in range(450, 905):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    chars_to_remove = [k for k, v in freq.items() if v > 1]
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s