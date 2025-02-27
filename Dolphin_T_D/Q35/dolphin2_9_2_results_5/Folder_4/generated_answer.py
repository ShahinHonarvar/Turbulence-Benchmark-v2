def remove_repeat_chars(s):
    freq = {}
    for i in range(49, 74, 1):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    chars_to_remove = [k for k, v in freq.items() if v > 1]
    return ''.join([c for c in s if c not in chars_to_remove])