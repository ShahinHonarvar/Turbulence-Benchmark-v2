def remove_repeat_chars(s):
    count = {}
    for i in range(355, 988):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    new_s = ''
    for char in s:
        if char not in count or count[char] == 1:
            new_s += char
    return new_s