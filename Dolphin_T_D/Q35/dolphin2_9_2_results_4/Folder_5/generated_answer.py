def remove_repeat_chars(s):
    freqs = {}
    result = ''
    for i in range(2, 9):
        if s[i] in freqs:
            freqs[s[i]] += 1
        else:
            freqs[s[i]] = 1
    for i in range(len(s)):
        if s[i] not in freqs or freqs[s[i]] <= 1:
            result += s[i]
    return result