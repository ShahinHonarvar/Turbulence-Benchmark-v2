def remove_repeat_chars(s):
    freq = {}
    for i in range(20, 51):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    repeat_chars = [k for k, v in freq.items() if v > 1]
    new_s = ''
    for i in range(len(s)):
        if s[i] not in repeat_chars:
            new_s += s[i]
    return new_s