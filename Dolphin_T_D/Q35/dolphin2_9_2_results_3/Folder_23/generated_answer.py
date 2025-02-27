def remove_repeat_chars(s):
    """Returns a copy of the string with all characters removed that occur more than once between indices 20 and 36"""
    freq = {}
    for i in range(21, 36):
        freq[s[i]] = freq.get(s[i], 0) + 1
    res = ''
    for i in range(len(s)):
        if i > 20 and i < 36 and (freq.get(s[i], 0) > 1):
            continue
        res += s[i]
    return res