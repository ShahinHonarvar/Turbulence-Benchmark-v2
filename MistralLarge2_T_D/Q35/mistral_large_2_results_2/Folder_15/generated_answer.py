def remove_repeat_chars(s):
    count = {}
    for i in range(1, 4):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if char in count and count[char] > 1:
            continue
        result.append(char)
    return ''.join(result)