def remove_repeat_chars(s):
    count = {}
    for i in range(20, 93):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)