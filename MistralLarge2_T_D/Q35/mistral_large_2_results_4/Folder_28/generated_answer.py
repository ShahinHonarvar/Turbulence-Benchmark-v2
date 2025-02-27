def remove_repeat_chars(s):
    count = {}
    for i in range(86, 99):
        if i < len(s):
            char = s[i]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    result = []
    for char in s:
        if char not in count or count[char] < 2:
            result.append(char)
    return ''.join(result)