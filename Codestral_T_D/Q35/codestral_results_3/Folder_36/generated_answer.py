def remove_repeat_chars(s):
    count = {}
    for i in range(477, 709):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    res = ''
    for char in s:
        if char not in count or count[char] == 1:
            res += char
    return res