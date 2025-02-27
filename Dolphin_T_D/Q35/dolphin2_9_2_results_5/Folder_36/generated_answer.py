def remove_repeat_chars(s):
    chars = {}
    for i in range(476, 710):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    result = ''
    for c in s:
        if chars[c] == 1:
            result += c
    return result