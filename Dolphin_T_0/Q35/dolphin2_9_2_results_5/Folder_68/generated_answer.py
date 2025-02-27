def remove_repeat_chars(s):
    freq = {}
    for i in range(1, 10):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    chars_to_remove = [k for k, v in freq.items() if v > 1]
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s