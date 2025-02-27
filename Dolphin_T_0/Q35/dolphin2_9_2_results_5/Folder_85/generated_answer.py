def remove_repeat_chars(s):
    chars = {}
    for i in range(1, 8):
        ch = s[i]
        if ch in chars and chars[ch] < 2:
            chars[ch] += 1
        else:
            chars[ch] = 1
    res = ''
    for ch in s:
        if ch in chars and chars[ch] < 2:
            res += ch
        else:
            res += ch
    return res