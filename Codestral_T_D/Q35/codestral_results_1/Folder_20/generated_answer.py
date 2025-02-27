def remove_repeat_chars(s):
    count = {}
    for i in range(27, 96):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for char in s:
        if char in count and count[char] > 1:
            count[char] = 0
        else:
            result += char
    return result